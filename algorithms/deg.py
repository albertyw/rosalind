# Degree Array
# http://rosalind.info/problems/deg/

from collections import defaultdict


def deg(data):
    vertexes = defaultdict(int)
    for x, y in data[1:]:
        vertexes[x] += 1
        vertexes[y] += 1
    return [vertexes[x] for x in range(1, data[0][0]+1)]

def parse_edge_list(data):
    data = data.split("\n")
    data = [[int(y) for y in x.split(' ')] for x in data if x != '']
    return data

if __name__ == '__main__':
    import sys
    file_location = sys.argv[1]
    with open(file_location, 'r') as file_handle:
        data = file_handle.read()
    data = parse_edge_list(data)
    output = deg(data)
    print(' '.join(str(x) for x in output))
