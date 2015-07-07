# Square in a Graph
# http://rosalind.info/problems/sq/

from collections import defaultdict

import inputparser

def search_graph(graph, path=[]):
    if len(path) == 5:
        return -1
    if path:
        nodes = graph[path[-1]]
    else:
        nodes = graph.keys()
    for node in nodes:
        if len(path) == 4 and path and path[0] == node:
            return 1
        if node in path:
            continue
        result = search_graph(graph, path + [node])
        if result == 1:
            return 1
    return -1

def check_square(data):
    graph = defaultdict(list)
    for line in data[1:]:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    return search_graph(graph)

def sq(data):
    output = []
    start = 2
    index = 2
    while index < len(data):
        if data[index] == [] or index == len(data)-1:
            output.append(check_square(data[start:index]))
            start = index+1
        index += 1
    return output

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = sq(data)
    print inputparser.space_separated(output)
