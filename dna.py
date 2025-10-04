from dependencies import *

def validateDNA(seq):
    #Validate a DNA sequence
    seq = seq.upper()
    for nuc in seq:
        if nuc not in Nucleotides:
            return False
    return True
    
def countingNucleotides(seq):
    #Count nucleotides within a DNA sequence
    nucDict = {"A":0, "C":0, "G":0, "T":0}
    for x in seq:
        nucDict[f"{x}"] += 1
    return(nucDict)

def transcription(seq):
    #Transcription of a DNA sequence into an RNA one
    seq = seq.replace("T", "U")
    return seq

def reverseComplement(seq):
    #Retrieve a complementary DNA strand
    nucComplement = {"A":"T","C":"G","T":"A","G":"C"}
    seq = list(seq)
    seq.reverse()
    seq = "".join(seq)
    complSeq = ""
    for nuc in seq:
        complSeq += nucComplement[nuc]
    return complSeq

def GC_Content(seq):
    #Calculate GC content in a DNA sequence
    nucAmount = len(seq)
    GC_amount = 0
    for i in seq:
        if i == "G" or i == "C":
            GC_amount +=1
    return GC_amount/nucAmount*100

def Count_Point_Mutations(seq1, seq2):
    #Calculate the amount of point mutations between two DNA strands
    length = len(seq1)
    Hamming_distance = 0
    i = 0
    while i < length:
        if seq1[i] != seq2[i]:
            Hamming_distance+=1
        i+=1
    return Hamming_distance

def motif(string, motif):
    #Find the positions of a given motif in a sequence
    positions = []
    start = 0
    while start < len(string):
        if string[start : start + len(motif)] == motif:
            positions.append(start+1)
        start+=1
    return positions
        
        

