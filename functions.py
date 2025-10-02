from dependencies import *
from dna import *

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