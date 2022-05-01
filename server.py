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
                if route['destination'] == destination:
                    return route
            return None

    def start_server(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        host = '10.4.1.124'
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
        self.adjacency_list.print_graph()
        self.adjacency_list.print_adjacency_list()
    
    def connect_nodes(self, new_node):
        if(len(self.adjacency_list.adj) < 1):
            self.adjacency_list.add_node(new_node)
            print("Name of node 0:" + self.adjacency_list.adj[0].name)
            print('Not enough nodes to connect')
            return

        num = random.randint(0, len(self.adjacency_list.adj)-1)

        random_node1 = self.adjacency_list.adj[0]

        if len(self.adjacency_list.adj) > 2:
            random_node2 = random_node1
            num = random.randint(0, len(self.adjacency_list.adj)-1)
            while random_node2 == random_node1:
                num = random.randint(0, len(self.adjacency_list.adj)-1)
                random_node2 = self.adjacency_list.adj[num]
            
            random_node2 = self.adjacency_list.adj[num]

            self.adjacency_list.add_edge(new_node, random_node2, 0)
            self.adjacency_list.add_edge(random_node2, new_node, 0)

            #new_node.add_route({'source':new_node.name, 'destination':random_node2.name, 'cost':random.randint(1,100)})
            #random_node2.add_route({'source':random_node2.name, 'destination':new_node.name, 'cost':random.randint(1,100)})
        
        #new_node.add_route({'source':new_node.name, 'destination':random_node1.name, 'cost':random.randint(1,100)})
        #random_node1.add_route({'source':random_node1.name, 'destination':new_node.name, 'cost':random.randint(1,100)})
    
        self.adjacency_list.add_edge(new_node, random_node1, 0)
        self.adjacency_list.add_edge(random_node1, new_node, 0)

        self.adjacency_list.print_graph()

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

                    cost = 0
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
                        
                        index = (index + 1) % 4
                    

                    print("Path from "+str(data['src'])+" to "+str(data['dest'])+": "+str(path))
                    data['path'] = path

                    self.specific_broadcast(json.dumps(data).encode(), data['path'][0])
                else:
                    self.specific_broadcast(json.dumps(data).encode(), data['path'][0])

server = Server()
