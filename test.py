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
    
    


test()

