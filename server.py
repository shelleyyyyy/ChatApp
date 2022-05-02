import socket
import threading
import json
import random
from adjacency_list import adjacency_list

class Server:
    def __init__(self):
        self.start_server()

    class Node:
        def __init__(self, name, address):
            self.name = name
            self.address = address
            self.routes = []
            self.bandwidth = 0
            self.distance = 0
            self.weight = 0
        
        def add_route(self, route):
            self.routes.append(route)
        
        def get_route(self, destination):
            for route in self.routes:
                if route[0].name == destination:
                    return route
            return None

    def start_server(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        host = '144.75.133.23'
        port = int(input('Enter port to run the server on --> '))

        self.routes = [{'souce':'bole', 'destination':'caveman', 'cost':100}, 
            {'souce':'caveman', 'destination':'biller', 'cost':25}, 
            {'souce':'biller', 'destination':'goe', 'cost':50}, 
            {'souce':'goe', 'destination':'bole', 'cost':75}]

        self.clients = []
        self.nodes = []
        self.adjacency_list = adjacency_list(0)

        self.s.bind((host,port))
        self.s.listen(100)
    
        print('Running on host: '+str(host))
        print('Running on port: '+str(port))

        self.username_lookup = {}

        while True:
            c, addr = self.s.accept()
            #print(c.getsockname())
            #print(c.getpeername()[0])
            username = c.recv(1024).decode()
            node = self.Node(username, c.getpeername()[0])
           

            self.username_lookup[c] = username
            
            self.clients.append((c, username))
            #print(self.username_lookup[c])
            threading.Thread(target=self.handle_client,args=(c,addr,node)).start()

    def broadcast(self,msg):
        for connection in self.clients:
            connection.send(msg)

    def specific_broadcast(self,msg, destination):
        for connection in self.clients:
            if connection[1] == destination:
                connection[0].send(msg)

    def connect_nodes_2(self, new_node):
        self.adjacency_list.on_new_node(new_node)
        self.adjacency_list.print_adjacency_list()

    def handle_client(self,c,addr, node):

        self.connect_nodes_2(new_node=node)

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

                    source_node = self.adjacency_list.get_node_by_name(data['source'])
                    if self.adjacency_list.get_node_by_name(data['destination']) == None:
                        print("FAIL")
                        msg = 'No User Name ' + data['destination'] + ' Found'
                        h = {
                            'src': str(data['source']),
                            'dest': str(data['destination']),
                            'msg': msg,
                            'path': [data['source']],
                        }
                        self.specific_broadcast(json.dumps(h).encode(), data['source'])
                    else:
                        destination_node = self.adjacency_list.get_node_by_name(data['destination'])

                        print('source_node: '+str(source_node.name))
                        print('destination_node: '+str(destination_node.name))
                        
                        weight_paths = self.adjacency_list.get_all_possible_paths(source_node, destination_node)
                        for path in weight_paths:
                            path.print_route()
                            print(" has weight of: " + str(path.weight))            
                        best_path = self.adjacency_list.return_best_path(weight_paths)

                        """ cost = 0
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
                                cost += route['cost']
                                path.append(route['destination'])
                                break 

                            if route['souce'] == source:
                                cost+= route['cost']
                                path.append(route['destination'])
                                source = route['destination']
                            
                            index = (index + 1) % 4 """
                        

                        print("Best path from "+str(data['source'])+" to "+str(data['destination'])+" has weight "+str(best_path.weight))

                        readable = []
                        for node in best_path.route:
                            readable.append(node.name)
                        readable.pop(0)

                        data['path'] = readable

                        print(readable)
                        print()
                        print("-------------------------------------------------------")
                        print()

                        self.specific_broadcast(json.dumps(data).encode(), data['path'][0])
                else:
                    self.specific_broadcast(json.dumps(data).encode(), data['path'][0])

server = Server()
