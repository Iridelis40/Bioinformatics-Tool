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

def ReadFile(filePath):
    #Retrieve a string from a text file containing a FASTA Format dataset
    with open(filePath, "r") as f:
        return [l.strip() for l in f.readlines()]
    
#dataset = ReadFile(filePath)

def GC_content_dataset(dataset):
    #Return the DNA strand with the most GC content in a dataset
    dataset_string = "".join(dataset)
    dataset_string = dataset_string.split(">")
    data_dict = {}
    for i in dataset_string:
        data_dict.update({f"{i[0:13]}":f"{i[13:]}"})
    data_dict.pop("")   
    for i in data_dict:
        data_dict[i]=GC_Content(data_dict[i])
    value_list = list(data_dict.values())
    value_list.sort(reverse=True)
    seq_name = ""
    for i in data_dict:
        if data_dict[i]==value_list[0]:
            seq_name = i
    return f"{seq_name}\n{value_list[0]}"

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
        
 

