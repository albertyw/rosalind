# Functions for parsing rosalind functions

from collections import defaultdict
import sys

def read_file():
    with open(sys.argv[1], 'r') as file_handle:
        data = file_handle.read().strip()
    return data

def parse_edge_list(data):
    data = [[int(x) for x in line.split()] for line in data.split("\n")]
    return data

def space_separated(data):
    return " ".join(str(x) for x in data)

def create_graph(data, undirected = True):
    graph = defaultdict(list)
    for line in data[1:]:
        graph[line[0]].append(line[1])
        if undirected:
            graph[line[1]].append(line[0])
    return graph

def parse_multiple_graphs(data):
    graphs = []
    start = 2
    index = 2
    while index < len(data)+1:
        if index == len(data) or data[index] == []:
            graphs.append(data[start:index])
            start = index+1
        index += 1
    return graphs

def create_adjacency_list(graph):
    node_children = {}
    for node in range(1, graph[0][0]+1):
        node_children[node] = []
    for edge in graph[1:]:
        node_children[edge[0]].append(edge[1])
    return node_children
