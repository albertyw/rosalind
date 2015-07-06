# Insertion Sort
# http://rosalind.info/problems/ins/

def swap(array, j, k):
    temp = array[j]
    array[j] = array[k]
    array[k] = temp
    return array

def ins(array):
    swaps = 0
    n = len(array)
    for i in range(1, n):
        k = i
        while k > 0 and array[k] < array[k-1]:
            array = swap(array, k-1, k)
            swaps += 1
            k -= 1
    return array, swaps

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as file_handle:
        data = file_handle.read()
    data = data.split("\n")[1].split(" ")
    data = [int(x) for x in data]
    output, swaps = ins(data)
    #print " ".join(str(x) for x in output)
    print swaps
