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

        routes = [{'souce':'bole', 'destination':'caveman', 'cost':'100'}, 
            {'souce':'caveman', 'destination':'biller', 'cost':'25'}, 
            {'souce':'biller', 'destination':'Goe', 'cost':'50'}, 
            {'souce':'Goe', 'destination':'bole', 'cost':'75'}]

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
            print('New connection. Username: '+str(username))
            self.broadcast('New person joined the room. Username: '+username)

            self.username_lookup[c] = username
            
            self.clients.append(c)
            print(self.username_lookup[c])
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def broadcast(self,msg):
        for connection in self.clients:
            connection.send(msg.encode())

    def specific_broadcast(self,msg, destination):
        for connection in self.clients:
            if connection.getpeername()[0] == destination:
                connection.send(msg.encode())

    def handle_client(self,c,addr):
        while True:
            try:
                msg = c.recv(1024)
            except:
                c.shutdown(socket.SHUT_RDWR)
                self.clients.remove(c)
                
                print(str(self.username_lookup[c])+' left the room.')
                self.broadcast(str(self.username_lookup[c])+' has left the room.')

                break

            if msg.decode() != '':                
                data = json.loads(str(msg.decode()))
                
                print(str(data))
                
                print(str(data['dest']))
                
                for connection in self.clients:
                    if connection != c:
                        connection.send(msg)

server = Server()
