from adjacency_list import adjacency_list
import time

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

    list = adjacency_list(0)

    for x in range(0, 20):
        node = Node(str(x), 'test')
        list.on_new_node(node)

    list.print_adjacency_list()

    #first run
    node = list.get_node_by_name('0')
    node1 = list.get_node_by_name('15')
    #second run
    node2 = list.get_node_by_name('4')
    node3 = list.get_node_by_name('6')
    #third run
    node4 = list.get_node_by_name('10')
    node5 = list.get_node_by_name('5')
    #fourth run
    node6 = list.get_node_by_name('19')
    node7 = list.get_node_by_name('0')
    #fifth run
    node8 = list.get_node_by_name('3')
    node9 = list.get_node_by_name('8')

    total_time = 0

    start = time.time()
    weight_paths = list.get_all_possible_paths(node, node1)
    best_path = list.return_best_path(weight_paths)
    print("Length of weight paths: " + str(len(weight_paths)))
    print("Best path from "+str(node.name)+" to "+str(node1.name)+" has weight "+str(best_path.weight))
    end = time.time()
    total_time += end - start
    string = "Elapsed Time: " + str(end - start) + " seconds"
    f = open("test.txt", "a")
    f.write(string)
    f.write("\n")
    f.close()
    print("Elapsed Time: " + str(end - start))

    start = time.time()
    weight_paths = list.get_all_possible_paths(node2, node3)
    best_path = list.return_best_path(weight_paths)
    print("Length of weight paths: " + str(len(weight_paths)))
    print("Best path from "+str(node2.name)+" to "+str(node3.name)+" has weight "+str(best_path.weight))
    end = time.time()
    total_time += end - start
    string = "Elapsed Time: " + str(end - start) + " seconds"
    f = open("test.txt", "a")
    f.write(string)
    f.write("\n")
    f.close()
    print("Elapsed Time: " + str(end - start))

    start = time.time()
    weight_paths = list.get_all_possible_paths(node4, node5)
    best_path = list.return_best_path(weight_paths)
    print("Length of weight paths: " + str(len(weight_paths)))
    print("Best path from "+str(node4.name)+" to "+str(node5.name)+" has weight "+str(best_path.weight))
    end = time.time()
    total_time += end - start
    string = "Elapsed Time: " + str(end - start) + " seconds"
    f = open("test.txt", "a")
    f.write(string)
    f.write("\n")
    f.close()
    print("Elapsed Time: " + str(end - start))

    start = time.time()
    weight_paths = list.get_all_possible_paths(node6, node7)
    best_path = list.return_best_path(weight_paths)
    print("Length of weight paths: " + str(len(weight_paths)))
    print("Best path from "+str(node6.name)+" to "+str(node7.name)+" has weight "+str(best_path.weight))
    end = time.time()
    total_time += end - start
    string = "Elapsed Time: " + str(end - start) + " seconds"
    f = open("test.txt", "a")
    f.write(string)
    f.write("\n")
    f.close()
    print("Elapsed Time: " + str(end - start))

    start = time.time()
    weight_paths = list.get_all_possible_paths(node8, node9)
    best_path = list.return_best_path(weight_paths)
    print("Length of weight paths: " + str(len(weight_paths)))
    print("Best path from "+str(node8.name)+" to "+str(node9.name)+" has weight "+str(best_path.weight))
    end = time.time()
    total_time += end - start
    string = "Elapsed Time: " + str(end - start) + " seconds"
    f = open("test.txt", "a")
    f.write(string)
    f.write("\n")
    f.close()
    print("Elapsed Time: " + str(end - start))

    final = "Total Time: " + str(total_time)
    final1 = "Average Time: " + str(total_time/5)

    print("Total Time: " + str(total_time))
    print("Average Time: " + str(total_time/5))

    string = "Elapsed Time: " + str(end - start) + " seconds"
    f = open("test.txt", "a")
    f.write(final)
    f.write("\n")
    f.write(final1)
    f.write("\n")
    f.write("\n")
    f.close()




test()
    

