import random

class adjacency_list:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = []
        self.paths = []

    class path:
        def __init__(self, source, destination, route, weight):
            self.source = source
            self.destination = destination
            self.route = route
            self.weight = weight
        
        def add_route(self, node):
            self.route.append(node)

        def increase_weight(self, weight):
            self.weight += weight

        def print_route(self):
            for item in self.route:
                print(item.name, " -> ", end="")
    
    def add_node(self, node):
        self.adj.append(node)

    def get_paths(self):
        return self.paths

    def get_node_by_name(self, name):
        for node in self.adj:
            if node.name == name:
                return node
        return None
    
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
    
    def find_route(self, source, destination):
        source_index = self.find_index(source)
        destination_index = self.find_index(destination)
        if source_index == -1 or destination_index == -1:
            return None
        else:
            return self.adj[source_index].get_route(destination.name)

    def print_graph(self):
        for i in range(len(self.adj)):
            print(f"{i} -> {self.adj[i].name}")
        
    def print_adjacency_list(self):
        for node in self.adj:
            print(f"{node.name}" + ":", end="")
            for route in node.routes:
                print(f" -> {route[0].name}, weight: {route[1]}", end="")
            print("")

    def add_weight_to_paths(self, paths):
        new_group = []
        new_path = []
        for group in paths:
            new_path = []
            for path in group:
                node = self.get_node_by_name(path)
                new_path.append(node)
            new_group.append(new_path)
        weighted_paths = []
        for group in new_group:
            weighted_paths.append(self.get_weight(group))
        
        return weighted_paths

    def get_weight(self, path):
        weight = 0
        for i in range(len(path) - 1):
            temp = self.find_route(path[i], path[i + 1])[1]
            weight += temp

        return self.path(path[0], path[-1], path, weight)

    def return_best_path(self, paths):
        best_path = paths[0]
        for path in paths:
            if path.weight < best_path.weight:
                best_path = path
        return best_path


    def get_all_possible_paths(self, source, destination):
        self.printAllPaths(source, destination)
        f = open("path.txt", "r")
        paths = f.read().split("\n")
        new_paths = []
        for path in paths:
            new_paths.append(path[:-1].split(" "))
        new_paths = new_paths[:-1]
        print(new_paths)
        f.close()
        file = open("path.txt","r+")
        file.truncate(0)
        file.close()
        return self.add_weight_to_paths(new_paths)

    def printAllPaths(self, s, d):
        #self.paths = []
        # Mark all the vertices as not visited
        visited =[False]*(self.adj.__len__())
        #print("Visited: " + str(visited))
 
        # Create an array to store paths
        path = self.path(s, d, [], 0)
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

    def printAllPathsUtil(self, u, d, visited, path):
        index = self.find_index(u)
        # Mark the current node as visited and store in path
        visited[index]= True
        path.route.append(u.name)
        
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print ("Check", str(path.route))
            f = open("path.txt", "a")
            for item in path.route:
                f.write(item + " ")
            f.write("\n")
            f.close()
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for route in u.routes:
                if visited[self.find_index(route[0])] == False:
                    self.printAllPathsUtil(route[0], d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.route.pop()
        visited[index]= False
