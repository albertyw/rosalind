import re, urllib2
import sys
import os
sys.path.append(os.getcwd()+'/../')
from data import rna_codon_table

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

protein_string = dataset

# Get number of codon possibilities per amino
codon_possibilities = {}
for codon, amino in rna_codon_table.items():
    if amino in codon_possibilities.keys():
        codon_possibilities[amino] += 1
    else:
        codon_possibilities[amino] = 1

# Start counting possibilities
possibilities = 1
possibilities *= 3 # Stop codon
for amino in protein_string:
    if amino not in codon_possibilities.keys():
        continue
    possibilities *= codon_possibilities[amino]
    possibilities %= 10**6

print possibilities
