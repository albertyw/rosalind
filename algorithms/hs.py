# Heap Sort
# http://rosalind.info/problems/hs/

import hea
import inputparser

def swap(heap, x, y):
    temp = heap[x]
    heap[x] = heap[y]
    heap[y] = temp
    return heap

def hs(data):
    heap = [0] + hea.hea(data)
    end = len(heap)-1
    while end > 0:
        heap = swap(heap, 1, end)
        end -= 1
        index = 1
        while True:
            left_child = index*2
            right_child = left_child+1
            if right_child <= end and heap[right_child] > heap[left_child] and heap[index] < heap[right_child]:
                heap = swap(heap, index, right_child)
                index = right_child
            elif left_child <= end and heap[index] < heap[left_child]:
                heap = swap(heap, index, left_child)
                index = left_child
            elif right_child <= end and heap[index] < heap[right_child]:
                heap = swap(heap, index, right_child)
                index = right_child
            else:
                break
    return heap[1:]


if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = hs(data)
    print inputparser.space_separated(output)
