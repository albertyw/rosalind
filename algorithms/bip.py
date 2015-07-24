# Testing Bipartiteness
# http://rosalind.info/problems/bip/

import inputparser

def bipartite(graph):
    part0 = set([graph[0][0]])
    part1 = set([])
    subgraph = []
    for edge in graph:
        if edge[0] in part0:
            part1.add(edge[1])
        if edge[0] in part1:
            part0.add(edge[1])
        if edge[1] in part0:
            part1.add(edge[0])
        if edge[1] in part1:
            part0.add(edge[0])
        if edge[0] not in part0 and edge[0] not in part1:
            subgraph.append(edge)
    if part0 & part1:
        return -1
    if subgraph:
        return bipartite(subgraph)
    return 1

def bip(data):
    graphs = inputparser.parse_multiple_graphs(data)
    return [bipartite(graph[1:]) for graph in graphs]

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = bip(data)
    print inputparser.space_separated(output)
