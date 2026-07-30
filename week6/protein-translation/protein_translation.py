mapping = {"Methionine" : ["AUG"], 
    "Phenylalanine" : ['UUU', 'UUC'], 
    "Leucine":['UUA', 'UUG'], 
    "Serine":['UCU', 'UCC', 'UCA', 'UCG'], 
    "Tyrosine":['UAU', 'UAC'], 
    "Cysteine":['UGU', 'UGC'],
    "Tryptophan":["UGG"],
    "STOP":['UAA', 'UAG', 'UGA']}

def proteins(strand):
    final_list = []

    while len(strand)>0:
        strand_3 = strand[0:3]
        strand = strand[3::]
        if strand_3 in mapping["STOP"]:
            return final_list
        for protein, test in mapping.items():
            if strand_3 in test:
                final_list.append(protein)
                
    return final_list
                
