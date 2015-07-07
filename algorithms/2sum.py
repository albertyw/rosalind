# 2SUM
# http://rosalind.info/problems/2sum/

import inputparser

def get2sum_for_numbers(line):
    groups = []
    index = 0
    while index < len(line):
        try:
            indexes = (index+1, line[index+1:].index(-line[index])+index+2)
            groups.append(indexes)
        except ValueError:
            pass
        index += 1
    if groups:
        groups = sorted(groups, key=lambda x: max(x))
        return groups[0]
    else:
        return [-1]


def get2sum(data):
    return [get2sum_for_numbers(line) for line in data[1:]]


if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = get2sum(data)
    for line in output:
        print inputparser.space_separated(line)
