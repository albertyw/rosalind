s = 'GATTGAAACAAGGATTAGGATATTATGTTGGGCTTTGCAGGTCTCCATGCCAATACCAGCTGCCCAACAAACTGGAGCTAATGACGCGGTTATGAATCGGGGATTCGTTGTTAACACGCGGACAGGACTAATCGACGCATTTGGAATGGTCTGCCAAGAGGTTCTACGTGTGATTGTGCTGCGCTCGACATCGAGTTTTAAGCTGAAAACGTTAACAAGATTCATATGGTAGTGTGACAATGTTGTTCTTTCAACAGCGTATACATCCACTATATGAGACGCACTCCAAAGTCGCCTTCTATCTTAATGGTTGGGGTAGAGTCCTGCTCATTCAAGACCACTGTAGATCATGTCCTTACCAACATTACTCTGTCTAAATACGGGAAAGCAGTTCGCTGGTCGGCCCCGTTTCACCTCCGCGCGCTGAAATGGGGCTACGCCCCTAGATTCCATGAGTGTGCGCCAACTGGCAGTTTCGAAACAGAACACACCCTGTTGACATATAGCGGAACCAGCGGTACCAGCTGGTCATTTAAAGATTGTACGAACCACGGATCTGTCAGGCACGACGAAAGTTGGAATACTTACCCAGATATGGGCAGGCGTAAGAAATTAGTAGTCAGAGTTCGTTGGATCCCAAGCTTTATGGACAGCTTGTTTGACAGCGTCTGAATGAACTTCAACGGAAGTATCCGGTTTAAGTGCTCAACTAGACACCTTAAATTAGCGATGCTCCTCCGACAGATCGCGGTCTACCGGTCTCAAGAAGGGAGATCACGCGTAGTTCGTATCTCCAAAACGCCTTACCGCGACCGTCTCTTTGGATTAGTAGGGGAAACTAACAAGTCGCAATAGGAACACAGCTATCGCGGGGTATGATGCGATTTCATACCGGTCATCACGGTGCATTTTCGGCAACACGTGAACAGATATCCTGCTCGTTCACACTGTGCTAGGTCAATATTCATTCCTCCATGGTAT'

a = s.count('A')
c = s.count('C')
g = s.count('G')
t = s.count('T')
print 'A', a
print 'C', c
print 'G', g
print 'T', t
print 'Total', len(s)
print str(a)+' '+str(c)+' '+str(g)+' '+str(t)