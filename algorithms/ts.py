# Topological Sorting
# http://rosalind.info/problems/ts/

from dag import topological_sort

import inputparser

def ts(data):
    return topological_sort(data)[::-1]

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = ts(data)
    print inputparser.space_separated(output)
