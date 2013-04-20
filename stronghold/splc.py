import sys
import os
sys.path.append(os.getcwd()+'/../')
from fasta import Fasta
from revc import complement
from prot import translate
from rna import transcribe

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

# Set up data structures
fasta = Fasta(dataset)
sequence = fasta.sequences[0]
introns = fasta.sequences[1:]

def get_exon(sequence, introns):
    for intron in introns:
        sequence = sequence.replace(intron, '')
    return sequence

if __name__ == '__main__':
    exon = get_exon(sequence, introns)
    rna_string = transcribe(exon)
    protein_string = translate(rna_string)
    print protein_string
