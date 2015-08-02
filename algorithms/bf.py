# Bellman-Ford Algorithm
# http://rosalind.info/problems/bf/

import sys

import inputparser


def bf(data):
    vertices = range(1, data[0][0]+1)
    source = 1
    predecessors = {}
    distances = {}

    for vertex in vertices:
        distances[vertex] = 'x'
        predecessors[vertex] = None
    distances[source] = 0

    for i in range(1, len(vertices)):
        for edge in data[1:]:
            if distances[edge[0]] != 'x' and (distances[edge[0]] + edge[2] < distances[edge[1]] or distances[edge[1]] == 'x'):
                distances[edge[1]] = distances[edge[0]] + edge[2]
                predecessors[edge[1]] = edge[0]

    for edge in data[1:]:
        if distances[edge[0]] != 'x' and distances[edge[1]] != 'x' and distances[edge[0]] + edge[2] < distances[edge[1]]:
            raise ValueError("Graph contains negative cycles")

    return [distances[edge] for edge in vertices]

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = bf(data)
    print inputparser.space_separated(output)


