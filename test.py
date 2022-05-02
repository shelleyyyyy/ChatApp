from adjacency_list import adjacency_list

class Node:
        def __init__(self, name, address):
            self.name = name
            self.address = address
            self.routes = []
            self.visited = False
        
        def add_route(self, route):
            self.routes.append(route)
        
        def get_route(self, destination):
            print("Destination: " + destination)
            for route in self.routes:
                if route[0] == destination:
                    print("Found route" + str(route[0]))
                    return route
            return None
            
def test():
    node = Node('bole', 'test')
    node1 = Node('caveman', 'test')
    node2 = Node('biller', 'test')
    node3 = Node('goe', 'test')

    list = adjacency_list(0)
    list.on_new_node(node)
    list.on_new_node(node1)
    list.on_new_node(node2)
    list.on_new_node(node3)

    list.print_adjacency_list()

    list.printAllPaths(node, node3)
    f = open("path.txt", "r")
    paths = f.read().split("\n")
    new_paths = []
    for path in paths:
        new_paths.append(path.split(" "))
    print(new_paths)
    f.close()

    file = open("path.txt","r+")
    file.truncate(0)
    file.close()
    
    


test()

