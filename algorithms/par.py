# 2-Way Partition
# http://rosalind.info/problems/par/

import inputparser

def par(data):
    pivot = data[1][0]
    less = []
    equal = []
    more = []
    for x in data[1]:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            more.append(x)
    return less + equal + more

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = par(data)
    print inputparser.space_separated(output)

