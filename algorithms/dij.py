# Dijkstra's Algorithm
# http://rosalind.info/problems/dij/

import sys

import inputparser

def find_current_node(unvisited, distances):
    min_distance = sys.maxint
    min_node = None
    for node in unvisited:
        if distances[node] < min_distance:
            min_distance = distances[node]
            min_node = node
    return min_node

def dij(data):
    unvisited = list(range(1, data[0][0]+1))
    distances = {}
    for node in unvisited:
        distances[node] = sys.maxint
    distances[1] = 0

    while unvisited:
        current_node = find_current_node(unvisited, distances)
        if not current_node:
            break
        unvisited.remove(current_node)
        for edge in data[1:]:
            if edge[0] == current_node:
                distances[edge[1]] = min(distances[edge[1]], distances[edge[0]]+edge[2])

    for node in distances:
        if distances[node] == sys.maxint:
            distances[node] = -1

    return [distances[node] for node in range(1, data[0][0]+1)]

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = dij(data)
    print inputparser.space_separated(output)
