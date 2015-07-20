# Building a Heap
# http://rosalind.info/problems/hea/

import inputparser

def hea(data):
    heap = [0]
    for val in data[1]:
        heap.append(val)
        index = len(heap)-1
        while heap[index/2] < heap[index] and index/2 > 0:
            temp = heap[index/2]
            heap[index/2] = heap[index]
            heap[index] = temp
            index = index/2
        #print heap
    return heap[1:]

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = hea(data)
    print inputparser.space_separated(output)