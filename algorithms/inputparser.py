# Functions for parsing rosalind functions

import sys

def read_file():
    with open(sys.argv[1], 'r') as file_handle:
        data = file_handle.read().strip()
    return data

def parse_edge_list(data):
    data = [[int(x) for x in line.split(" ")] for line in data.split("\n")]
    return data

def space_separated(data):
    return " ".join(str(x) for x in data)
