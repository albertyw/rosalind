# 3-Way Partition
# http://rosalind.info/problems/par3/

import inputparser
import par

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = par.par(data)
    print inputparser.space_separated(output)


