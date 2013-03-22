import sys
import os
sys.path.append(os.getcwd()+'/../')
from fasta import Fasta

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

# Set up data structures
fasta = Fasta(dataset)
length = len(fasta.data[fasta.data.keys()[0]])
profile_matrix = {}
for base in ['A', 'C', 'G','T']:
    profile_matrix[base] = [0]*length

# Compute profile matrix
for sequence_id, sequence_string in fasta.data.items():
    i = 0
    while i < len(sequence_string):
        profile_matrix[sequence_string[i]][i] += 1
        i += 1
    
# Compute consensus string
consensus_string = ''
i = 0
while i < length:
    best = 0
    best_base = 'A'
    for base in ['A', 'C', 'G','T']:
        if best < profile_matrix[base][i]:
            best = profile_matrix[base][i]
            best_base = base
    consensus_string += best_base
    i += 1

# Output consensus string
print consensus_string

# Output profile matrix
for base in ['A', 'C', 'G','T']:
    line = base+": "
    for i in profile_matrix[base]:
        line += str(i)+' '
    print line
