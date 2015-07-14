# Breadth-First Search
# http://rosalind.info/problems/bfs/

import inputparser

def bfs(data):
    graph = inputparser.create_graph(data, False)
    distances = [-1] * data[0][0]
    distances[0] = 0
    search_nodes = [1]
    found_nodes = []
    distance = 1
    while search_nodes:
        for node in search_nodes:
            for found_node in graph[node]:
                if distances[found_node-1] == -1:
                    found_nodes.append(found_node)
                    distances[found_node-1] = distance
        distance += 1
        search_nodes = found_nodes
        found_nodes = []
    return distances


if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = bfs(data)
    print inputparser.space_separated(output)
