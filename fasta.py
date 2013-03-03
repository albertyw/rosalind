"""
Yet another FASTA class

Every string in a FASTA file begins with a single-line that contains the symbol 
'>' along with some labeling information about the string. The word following 
the '>' symbol is the identifier of the sequence, and the rest of the line is 
its description (both are optional). There should be no space between the ">" 
and the first letter of the identifier.

All subsequent lines contain the string itself; it is recommended that all lines 
of text are shorter than 80 symbols. The string ends when another line starting 
with '>' appears, indicating the start of another sequence (or if the end of the 
file is reached).
"""

class Fasta:
    def __init__(self, string):
        self.data = {}
        self.description = {}
        self.parse(string)
        
    def parse(self, string):
        # Turn into list
        string = string.replace("\r", "\n")
        lines = string.split("\n")
        lines = [v for v in lines if v != '']
        
        # Split into sequences
        sequence = []
        for line in lines:
            if line[0] == '>' and sequence != []:
                self.add_data(sequence)
                sequence = []
            sequence.append(line)
        self.add_data(sequence)
        
        
    def add_data(self, sequence):
        if len(sequence[0]) > 1:
            index = sequence[0].find(' ')
            if index != -1:
                sequence_id = sequence[0][1:index]
                sequence_description = sequence[0][index+1:]
            else:
                sequence_id = sequence[0][1:]
                sequence_description = ''
        else:
            sequence_id = str(len(self.data)+1)
            sequence_description = ''
        sequence_data = ''.join(sequence[1:])
        self.data[sequence_id] = sequence_data
        self.description[sequence_id] = sequence_description
        
        