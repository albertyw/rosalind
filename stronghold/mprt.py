import re, urllib2
import sys
import os
sys.path.append(os.getcwd()+'/../')
from fasta import Fasta

scratch_handle = open('../scratch.txt','r')
dataset = scratch_handle.read()
scratch_handle.close()

# Download the FASTA file for the uniprot
def get_fasta(uniprot_id):
    u = urllib2.urlopen('http://www.uniprot.org/uniprot/'+uniprot_id+'.fasta')
    fasta = Fasta(u.read())
    return fasta

# Convert the motif into a regex expression
motif_matching = "N{P}[ST]{P}"
new_motif = ''
for char in motif_matching:
    if char == '{':
        new_motif += '[^'
    elif char == '}':
        new_motif += ']'
    else:
        new_motif += char
motif_matching = re.compile('(?=('+new_motif+'))')

# Do the search
for uniprot_id in dataset.split("\n"):
    if uniprot_id == '':
        continue
    fasta = get_fasta(uniprot_id)
    fasta_id, sequence = fasta.data.items()[0]
    start_locations = ''
    for match in motif_matching.finditer(sequence):
        start_locations += str(match.start()+1)+' '
    if start_locations != '':
        print uniprot_id
        print start_locations[:-1]
