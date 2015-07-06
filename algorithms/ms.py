# Merge Sort
# http://rosalind.info/problems/ms/

from mer import mer

def ms(array):
    array1 = array[0:len(array)/2]
    array2 = array[len(array)/2:]
    if len(array1) > 1:
        array1 = ms(array1)
    if len(array2) > 1:
        array2 = ms(array2)
    array = mer(array1, array2)
    return array

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as file_handle:
        data = file_handle.read()
        data = [line.split(" ") for line in data.split("\n")]
        data = [int(x) for x in data[1]]
        output = ms(data)
        print " ".join(str(x) for x in output)
