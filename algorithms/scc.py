# Strongly Connected Components
# http://rosalind.info/problems/scc/

import inputparser

def get_unfound_vertex(vertexes, total_vertexes):
    for x in range(1, total_vertexes+1):
        if x not in vertexes:
            return x
    return None

def dfs(adjacencies, vertex, path = None):
    if not path:
        path = [vertex]
    next_vertexes = [x for x in adjacencies[vertex] if x not in path]
    print path, next_vertexes
    if not next_vertexes:
        return path
    path.append(next_vertexes[0])
    return dfs(adjacencies, next_vertexes[0], path)

def scc(graph):
    vertexes = []
    while get_unfound_vertex(vertexes, graph[0][0]):
        vertex = get_unfound_vertex(vertexes, graph[0][0])
        adjacencies = inputparser.create_adjacency_list(graph)
        for reached_vertex in dfs(adjacencies, vertex):
            vertexes.append(reached_vertex)
    print vertexes
    return vertexes



import sys
import time
import resource
from itertools import groupby
from collections import defaultdict


#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


class Track(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()


def dfs(graph_dict, node, track):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail node: [head nodes]}. Depth first search runs recrusively and keeps
    track of the parameters"""

    track.explored.add(node)
    track.leader[node] = track.current_source
    for head in graph_dict[node]:
        if head not in track.explored:
            dfs(graph_dict, head, track)
    track.current_time += 1
    track.finish_time[node] = track.current_time


def dfs_loop(graph_dict, nodes, track):
    """Outter loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""

    for node in nodes:
        if node not in track.explored:
            track.current_source = node
            dfs(graph_dict, node, track)


def scc(graph):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on orignial graph with nodes in decreasing finish
    time order(obatined from firt run). Return a dict of {leader: SCC}."""

    nodes = range(1, graph[0][0]+1)
    reverse_graph = inputparser.create_reverse_graph(graph)
    graph = inputparser.create_adjacency_list(graph)
    reverse_graph = inputparser.create_adjacency_list(reverse_graph)

    out = defaultdict(list)
    track = Track()
    dfs_loop(reverse_graph, nodes, track)
    sorted_nodes = sorted(track.finish_time,
                          key=track.finish_time.get, reverse=True)
    track.current_time = 0
    track.current_source = None
    track.explored = set()
    dfs_loop(graph, sorted_nodes, track)
    for lead, vertex in groupby(sorted(track.leader, key=track.leader.get),
                                key=track.leader.get):
        out[lead] = list(vertex)

    return [len(out)]
    return out



if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = scc(data)
    print inputparser.space_separated(output)
