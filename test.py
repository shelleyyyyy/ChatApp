from adjacency_list import adjacency_list

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

def test():
    node = Node('bole', 'test')
    node1 = Node('caveman', 'test')
    node2 = Node('biller', 'test')

    list = adjacency_list(0)
    list.add_node(node)
    list.add_node(node1)
    list.add_node(node2)

    list.add_edge(node, node1, 100)

    list.print_graph()

test()

