# Double-Degree Array
# http://rosalind.info/problems/ddeg/

from collections import defaultdict

from deg import deg

def ddeg(data):
    degrees = deg(data)
    vertexes = defaultdict(int)
    for x, y in data[1:]:
        vertexes[x] += degrees[y-1]
        vertexes[y] += degrees[x-1]
    return [vertexes[x] for x in range(1, data[0][0]+1)]


if __name__ == '__main__':
    import sys
    from deg import parse_edge_list
    file_location = sys.argv[1]
    with open(file_location, 'r') as file_handle:
        data = file_handle.read()
    data = parse_edge_list(data)
    output = ddeg(data)
    print(' '.join(str(x) for x in output))
