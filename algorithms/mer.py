# Merge Two Sorted Arrays
# http://rosalind.info/problems/mer/

def mer(array1, array2):
    merged = []
    while len(array1) > 0 or len(array2) > 0:
        if len(array1) == 0:
            merged += array2
            array2 = []
        elif len(array2) == 0:
            merged += array1
            array1 = []
        elif array1[0] > array2[0]:
            merged.append(array2.pop(0))
        else:
            merged.append(array1.pop(0))
    return merged

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as file_handle:
        data = file_handle.read()
    data = [line.split(" ") for line in data.split("\n")]
    array1 = [int(x) for x in data[1]]
    array2 = [int(x) for x in data[3]]
    output = mer(array1, array2)
    print " ".join(str(x) for x in output)
