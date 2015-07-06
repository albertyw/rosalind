# Majority Element
# http://rosalind.info/problems/maj/

from collections import defaultdict

def majority(line):
    elements = defaultdict(int)
    for x in line:
        elements[x] += 1
        if elements[x] > len(line)/2:
            return x
    return -1

def maj(data):
    return [majority(line) for line in data]

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as file_handle:
        data = file_handle.read()
    data = [line.split(" ") for line in data.split("\n")]
    output = maj(data[1:])
    print " ".join(str(x) for x in output)
