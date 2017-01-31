from f_importerGraph import *

def dijkstra(graph_dict, start, end):
    print("Graph used: ",graph_dict)
    # create empty dictionary to hold the distance of each node to the start node
    distances = {}

    # create empty dict to hold the predecessor of each node
    predecessors = {}

    # set all initial distances to infinity
    #  and no predecessor for any node
    for node in graph_dict:
        distances[node] = float('inf')
        predecessors[node] = None
    print()
    # create empty list for nodes that have been visited with permanent distance
    labelled_nodes = []

    # set the distance from the start node to be 0
    distances[start] = 0

    # as long as there are still nodes to assess:
    while len(labelled_nodes) < len(graph_dict):

        # create empty dict for nodes that are still available
        still_in = {}
        for node in graph_dict:
            if node not in labelled_nodes:
                still_in[node] = distances[node]

        # find the node with the lowest distance to the current node
        lowest = float('inf')
        for each in still_in:
            if still_in.get(each) < lowest:
                lowest = still_in.get(each)
                closest = each
        # and add it to the permanently labelled nodes
        labelled_nodes.append(closest)

        # if node is a neighbor of closest
        for node in graph_dict[closest]:
            if graph_dict[closest].get(node) != None:
                # if a shorter path to that node can be found
                if distances[node] > distances[closest] + graph_dict[closest].get(node):
                # update the distance with that shorter distance
                    distances[node] = distances[closest] + graph_dict[closest].get(node)
                # set the predecessor for that node
                    predecessors[node] = closest

    path = [end]
    while start not in path:
        path.append(predecessors[path[-1]]) #find and append the predecessor of the last node in path

    # the 'predecessors' dictionary can be used to find next direction as long as the client is following path
    # if the client goes off-path it's location should be located again and a new path should be calculated.


    # return the path with distance
    return path[::-1], distances[end]

#graph = {'RPI_AP1':{'RPI_AP2':1, 'RPI_AP3':3},'RPI_AP2':{'RPI_AP1':1, 'RPI_AP3':3}, 'RPI_AP3':{'RPI_AP1':3, 'RPI_AP2':3}}
#graph2 = {'A': {'B':1, 'D':5}, 'B': {'A':1, 'C':2, 'H':1}, 'C':{'B':2, 'D':3}, 'D':{'A':5, 'C':3, 'E':1}, 'E':{'D':1, 'F':3}, 'F':{'E':3, 'G':2}, 'G':{'F':2}, 'H':{'B':1, 'I':2}, 'I':{'H':2, 'J':1}, 'J':{'I':1}}
graph = import_graph()
startnode = input('RPI_AP2')
endnode = input('RPI_AP3')
print(startnode, endnode)
print(dijkstra(graph, startnode, endnode))
