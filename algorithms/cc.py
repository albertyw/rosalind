# Connected Components
# http://rosalind.info/problems/cc/

def cc(data):
    groups = []
    for x in range(1, int(data[0][0])+1):
        groups.append([str(x)])
    for link in data[1:]:
        grouped = []
        i = 0
        while i < len(groups):
            if link[0] in groups[i] or link[1] in groups[i]:
                grouped += groups.pop(i)
            else:
                i += 1
        groups.append(grouped)
    return len(groups)


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as file_handle:
        data = file_handle.read().strip()
    data = [line.split(" ") for line in data.split("\n")]
    output = cc(data[0:])
    print output

