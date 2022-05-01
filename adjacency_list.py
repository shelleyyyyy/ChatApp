import random

class adjacency_list:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = []
    
    def add_node(self, node):
        self.adj.append(node)
    
    def on_new_node(self, node):
        self.add_node(node)

        if(len(self.adj) != 1):
            random_node1 = self.get_random_node()
            while random_node1.name == node.name:
                random_node1 = self.get_random_node()
        
        if(len(self.adj) > 2):
            random_node2 = self.get_random_node()
            while random_node2.name == random_node1.name or random_node2.name == node.name:
                random_node2 = self.get_random_node()
            self.connect(node, random_node2, self.generate_random_weight())
            self.connect(node, random_node1, self.generate_random_weight())
        elif(len(self.adj) > 1):
            self.connect(node, random_node1, self.generate_random_weight())
        else:
            print("No nodes to connect to yet")
    
    def generate_random_weight(self):
        return random.randint(1, 100)

    def get_random_node(self):
        return self.adj[random.randint(0, len(self.adj) - 1)]

    def connect(self, node1, node2, weight):
        self.add_edge(node1, node2, weight)
        self.add_edge(node2, node1, weight)

    def add_edge(self, source_node, destination_node, weight):
        source_index = self.find_index(source_node)
        self.adj[source_index].routes.append((destination_node, weight))

    def find_index(self, node):
        for i in range(len(self.adj)):
            if self.adj[i].name == node.name:
                return i
        return -1

    def print_graph(self):
        for i in range(len(self.adj)):
            print(f"{i} -> {self.adj[i].name}")
        
    def print_adjacency_list(self):
        for node in self.adj:
            print(f"{node.name}" + ":", end="")
            for route in node.routes:
                print(f" -> {route[0].name}, weight: {route[1]}", end="")
            print("")