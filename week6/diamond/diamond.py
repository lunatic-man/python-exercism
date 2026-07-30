import string

def rows(letter):
    final_diamond=[]
    index = string.ascii_uppercase.find(letter)
    half_diamond = []

    for i in range(index+1):
        if i==0:
            row = " "*index + string.ascii_uppercase[0] + " "*index
            half_diamond.append(row)
        elif i==index:
            row = string.ascii_uppercase[index] + " "*((index*2) -1) + string.ascii_uppercase[index]
            half_diamond.append(row)
        else:
            row = " "*(index-i) + string.ascii_uppercase[i] + " "*(i +(i-1))  + string.ascii_uppercase[i] + " "*(index-i)
            half_diamond.append(row)

    final_diamond.extend(half_diamond)

    lower_half_diamond = []

    for i in range(index, 0, -1):
        lower_half_diamond.append(half_diamond[i-1])

    final_diamond.extend(lower_half_diamond)

    return final_diamond
