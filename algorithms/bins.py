# Binary Search
# http://rosalind.info/problems/bins/

def binary_search(array, integer):
    index = len(array)/2
    if array[index] == integer:
        return index
    elif index == 0:
        return -1
    if array[index] > integer:
        return binary_search(array[0:index], integer)
    else:
        value = binary_search(array[index:], integer)
        if value != -1:
            value = value + index
        return value

def bins(array, integers):
    data = [binary_search(array, integer) for integer in integers]
    # 1-indexed, instead of 0-indexed
    def reindex(x):
        if x >= 0:
            x += 1
        return x
    return [reindex(x) for x in data]

def parse_data(data):
    data = data.split("\n")
    array = [int(i) for i in data[2].split(" ")]
    integers = [int(i) for i in data[3].split(" ")]
    return array, integers

if __name__ == b"__main__":
    import sys
    file_location = sys.argv[1]
    with open(file_location, 'r') as file_handle:
        array, integers = parse_data(file_handle.read())
    out = bins(array, integers)
    print(b' '.join(str(x) for x in out))
