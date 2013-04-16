import sys
import os
sys.path.append(os.getcwd()+'/../')
from fasta import Fasta
from revc import complement

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

# Set up data structures
fasta = Fasta(dataset)
sequence = fasta.data[fasta.data.keys()[0]]

def is_palindrome(sequence):
    if sequence == complement(sequence):
        return True
    return False

for length in range(4, 13):
    index = 0
    while index < len(sequence)-length+1:
        substring = sequence[index:index+length]
        if is_palindrome(substring):
            print index+1, length
        index += 1
