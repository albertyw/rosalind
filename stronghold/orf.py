import re, urllib2
import sys
import os
sys.path.append(os.getcwd()+'/../')
from fasta import Fasta
from data import rna_codon_table

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()


def complement(sc):
    sc = sc[::-1]
    sc = sc.replace('G', '1')
    sc = sc.replace('C', 'G')
    sc = sc.replace('1', 'C')

    sc = sc.replace('A', '1')
    sc = sc.replace('U', 'A')
    sc = sc.replace('1', 'U')
    return sc

def find_sequences(rna_string):
    offset = 0
    sequences = []
    while True:
        try:
            index = rna_string.index(start_codon, offset)
        except ValueError:
            break
        offset = index+1
        sequence = ''
        while index+3 <= len(dna_string):
            codon = rna_string[index:index+3]
            amino = rna_codon_table[codon]
            if amino == 'Stop':
                break
            sequence += amino
            index += 3
        if amino == 'Stop':
            sequences.append(sequence)
    return sequences

fasta = Fasta(dataset)
dna_string = fasta.data.values()[0]
rna_string = dna_string.replace('T', 'U')
start_codon = 'AUG'
sequences = find_sequences(rna_string)
sequences += find_sequences(complement(rna_string))
sequences = set(sequences)
for sequence in sequences:
    print sequence

