import sys
import os
sys.path.append(os.getcwd()+'/../')
from fasta import Fasta

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

k = 3

graph = []
fasta = Fasta(dataset)
for parent_id, parent_sequence in fasta.data.items():
    for child_id, child_sequence in fasta.data.items():
        if parent_id == child_id:
            continue
        if parent_sequence[-k:] == child_sequence[:k]:
            graph.append((parent_id, child_id))

for parent_id, child_id in graph:
    print parent_id, child_id

