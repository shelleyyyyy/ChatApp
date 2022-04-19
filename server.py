import socket
import threading
import json

class Server:
    def __init__(self):
        self.start_server()

    def start_server(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        host = '144.75.133.23'
        port = int(input('Enter port to run the server on --> '))

        self.routes = [{'souce':'bole', 'destination':'caveman', 'cost':'100'}, 
            {'souce':'caveman', 'destination':'biller', 'cost':'25'}, 
            {'souce':'biller', 'destination':'goe', 'cost':'50'}, 
            {'souce':'goe', 'destination':'bole', 'cost':'75'}]

        self.clients = []
        self.nodes = []

        self.s.bind((host,port))
        self.s.listen(100)
    
        print('Running on host: '+str(host))
        print('Running on port: '+str(port))

        self.username_lookup = {}

        while True:
            c, addr = self.s.accept()
            print(c)
            print(c.getsockname())
            print(c.getpeername()[0])
            username = c.recv(1024).decode()
           
            
            # print('New connection. Username: '+str(username))
            
            # h = {
            #     'msg': 'joined',
            #     'join': username,
            # }
            
            # j = json.dumps(h)
            
            # self.broadcast(j)

            self.username_lookup[c] = username
            
            self.clients.append((c, username))
            print(self.username_lookup[c])
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def broadcast(self,msg):
        for connection in self.clients:
            connection.send(msg)

    def specific_broadcast(self,msg, destination):
        for connection in self.clients:
            if connection[1] == destination:
                connection[0].send(msg)

    def handle_client(self,c,addr):
        while True:
            try:
                msg = c.recv(1024)
            except:
                c.shutdown(socket.SHUT_RDWR)
                self.clients.remove(c)
                
                print(str(self.username_lookup[c])+' left the room.')
                # self.broadcast(str(self.username_lookup[c])+' has left the room.')

                break

            if msg.decode() != '':

                data = json.loads(str(msg.decode()))

                if len(data['path']) == 0:

                    path = []
                    source = data['src']
                    if source == 'bole':
                        index = 0
                    elif source == 'caveman':
                        index = 1
                    elif source == 'biller':
                        index = 2
                    elif source == 'goe':
                        index = 3
                    else:
                        print('Invalid source')
                        continue
                    while True:
                        route = self.routes[index]
                        if route['destination'] == data['dest']:
                            path.append(route['destination'])
                            break 

                        if route['souce'] == source:
                            path.append(route['destination'])
                            source = route['destination']
                        
                        index = (index + 1) % 4
                    

                    print("Path from "+str(data['src'])+" to "+str(data['dest'])+": "+str(path))
                    data['path'] = path

                    self.specific_broadcast(json.dumps(data).encode(), data['path'][0])
                else:
                    self.specific_broadcast(json.dumps(data).encode(), data['path'][0])

server = Server()
