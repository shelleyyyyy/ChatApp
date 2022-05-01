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
                if route['destination'] == destination:
                    return route
            return None

def shortest_path(adj_list, source, destination):
    print("Shortest path from " + source.name + " to " + destination.name)
    return find_path(adj_list, source, destination, [source.name], [])


def find_path(list, source, destination, path, completed):
    print("Current path: " + str(path))
    if source.name == destination.name:
        completed.append(path)
    
    for route in source.routes:
        print("Current Souce: " + source.name)
        print("Looking at route: " + route[0].name)
        if route[0].name in path:
            continue
        path.append(route[0].name)
        print("Route: " + route[0].name + " added to path")
        find_path(list, route[0], destination, path, completed)

    return completed


            
            
    

def get_smallest_node(adj_list):
    smallest = adj_list.adj[0]
    for node in adj_list.adj:
        if node.distance < smallest.distance:
            smallest = node
    return smallest

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

    # Prints all paths from 's' to 'd'
    def printAllPaths(s, d):
 
        # Mark all the vertices as not visited
        visited =[False]*(list.adj.__len__())
        print("Visited: " + str(visited))
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        printAllPathsUtil(s, d, visited, path)

    def printAllPathsUtil(u, d, visited, path):
        
        index = list.find_index(u)
        # Mark the current node as visited and store in path
        visited[index]= True
        path.append(u.name)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print (path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for route in u.routes:
                if visited[list.find_index(route[0])] == False:
                    printAllPathsUtil(route[0], d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[index]= False

    print(printAllPaths(node, node3))
    


test()

