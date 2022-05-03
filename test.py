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
            for route in self.routes:
                if route[0].name == destination:
                    return route
            return None
            
def test():
    node = Node('bole', 'test')
    node1 = Node('caveman', 'test')
    node2 = Node('biller', 'test')
    node3 = Node('goe', 'test')
    node4 = Node('dan', 'test')

    list = adjacency_list(0)
    list.on_new_node(node)
    list.on_new_node(node1)
    #list.on_new_node(node2)
    #list.on_new_node(node3)
    #list.on_new_node(node4)

    list.print_adjacency_list()

    weight_paths = list.get_all_possible_paths(node, node1)
    for path in weight_paths:
        print(path.weight)
    best = list.return_best_path(weight_paths)
    print(best.weight)
    print(best.route)
    
def test2():
    nodeA = Node('A', 'test')
    nodeB = Node('B', 'test')
    nodeC = Node('C', 'test')
    nodeD = Node('D', 'test')
    nodeE = Node('E', 'test')

    list = adjacency_list(0)
    
    list.add_node(nodeA)
    list.add_node(nodeB)
    list.add_node(nodeC)
    list.add_node(nodeD)
    list.add_node(nodeE)

    #Node A Connections
    list.connect(nodeA, nodeB, 2)
    list.connect(nodeA, nodeC, 7)
    list.connect(nodeA, nodeD, 10)

    #Node B Connections
    list.connect(nodeB, nodeC, 3)
    list.connect(nodeB, nodeD, 6)
    list.connect(nodeB, nodeE, 3)

    #Node C Connections
    list.connect(nodeC, nodeD, 4)
    
    #Node D Connections
    list.connect(nodeD, nodeE, 1)

    list.print_adjacency_list()

    weight_paths = list.get_all_possible_paths(nodeA, nodeD)
    for path in weight_paths:
        path.print_route()
        print(" has weight of: " + str(path.weight)) 
    best_path = list.return_best_path(weight_paths)
    print("Best path from "+str(nodeA.name)+" to "+str(nodeD.name)+" has weight "+str(best_path.weight))






test2()

