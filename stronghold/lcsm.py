import sys
import os
sys.path.append(os.getcwd()+'/../')
from fasta import Fasta

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

fasta = Fasta(dataset)

# This is a slow longest common substring solution
sequences = [sequence for id, sequence in fasta.data.items()]

# find shortest sequence
shortest_sequence = ''
shortest_length = 99999999999
for sequence in sequences:
    if len(sequence) < shortest_length:
        shortest_sequence = sequence
        shortest_length = len(sequence)

# Find longest common substring (in a very inefficient manner)
length = shortest_length
common_substrings = []
while length > 0:
    offset = 0
    while offset + length <= len(shortest_sequence):
        substring = shortest_sequence[offset:offset+length]
        found = True
        for sequence in sequences:
            if substring not in sequence:
                found = False
                break
        if found == True:
            common_substrings.append(substring)
        offset += 1
    length -= 1

print common_substrings[0]
