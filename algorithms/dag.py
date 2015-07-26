# Testing Acyclicity
# http://rosalind.info/problems/dag/

from collections import defaultdict

import inputparser

def create_node_children(graph):
    node_children = defaultdict(list)
    for edge in graph[1:]:
        node_children[edge[0]].append(edge[1])
    return node_children

def topological_sort(graph):
    graph_sorted = []
    graph_unsorted = create_node_children(graph)

    while graph_unsorted:
        acyclic = False
        for node, edges in graph_unsorted.items():
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.append((node, edges))
        if not acyclic:
            raise RuntimeError("cyclic graph")
    return graph_sorted

def dag(data):
    graphs = inputparser.parse_multiple_graphs(data)
    acyclic = []
    for graph in graphs:
        try:
            topological_sort(graph)
            acyclic.append(1)
        except RuntimeError:
            acyclic.append(-1)
    return acyclic

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = dag(data)
    print inputparser.space_separated(output)
