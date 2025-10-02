from dependencies import *

def Translation(seq):
    #Translates  mRNA sequence into a protein string 
    RNA  = ""
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        symbol = codons[codon]
        if symbol == "Stop":
            break
        RNA += symbol
    return RNA

