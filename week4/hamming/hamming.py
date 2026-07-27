def distance(strand_a, strand_b):
    hamming_dist=0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        for i in range(0, len(strand_a)):
            if strand_a[i]!=strand_b[i]:
                hamming_dist+=1
    return hamming_dist
