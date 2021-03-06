import sys
import os
sys.path.append(os.getcwd()+'/../')
from data import amino_acid_mass

protein = "TQYYEEFYLICFMMNHLEGKMPEGCPQCIFYRFYCEMHNNIEMCICSWIKGDLEVSNQWWFRREEWQAEDSQLHYGMLHHHSNRDFATWLETNAPEAVMVSIGRWYALFFVDPYNLGVVVNQFEFYMMEFFGEPHKRAWHGWMDKNSHTFWGYFPWKECMEPIAVHKEIERVHTAHFRKQKYSWQSRLTLHPSTIHEFPIWIFEEGFEDGFGKMPETVDNIMRMYGMLWSWYRVVRTENCIEYLVEMAQPFKKNKCPPMEDMMKVEYCLLTRVLCWIPALKCVGGALCQIGPNMRGDWNSEHTMLLQFQLWAKEMVWANCKSQKQFISSDNAHTYMQQGLWVIHHINLWKARPMHDLQASNPVGEIGPRERPKTSNTDEDMWMIIVRNEEKPAADPWDARLQGIKKAMGVKCGARCDTWIMLIGFNCLKAAFLTGHPEKISNGIRHAHGEIFFNWERHCIMNQGLHMNKFEQCICCFPEVSQRYCFPPPVEMEKMVKHTDIGNKTQVERFKHWPEPWKQWHEWKFNSGQIMYAGMWYYKKALNPSIQFDFSSYYLHSVDKALETWQICYQADSCSCYFECRRWFKHYYFITITQQTWTSFLGGLMYTTVIYVPKMPYTSRLCNAGESEQFACIYFNETSWQARKWGRAMKHHQCCDIMTQAWTNMSWLKCGDKIDWGQNPSVCKTHMEGRIISRGDIMFEHFGTGKYEEAQMCLEPKPAEWHQRLFWWGNSNWRTLFTHMLVHATYSRMIGENDRVCPVSMICGRGWYPKGIWCFCFQGGICLEGCLDEQQRMVNNAQEPNWVFAQITNNCHCWWRLVRYNSIIKMCAQSLIHLPFMVYGCMVRCSSLRYYVATLEIAIQAWGLRANLIWNIQQVGSCSWMEHGMPHMYLHLQYHRKGACHCHTNNYENQFLCNYCHLWPVCRVQSYGQEQLYCCRSAERTLDGKMVFHMDWNFPVQCVGESAKLTQLYLAECPAVNCHSISS"

mass = 0 #amino_acid_mass["Water"]
for amino in protein:
    mass += amino_acid_mass[amino]
    
print mass

