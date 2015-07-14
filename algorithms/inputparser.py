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
    while index < len(data):
        if data[index] == [] or index == len(data)-1:
            graphs.append(data[start:index])
        index += 1
    return graphs
