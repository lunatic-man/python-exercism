SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def is_sublist(smaller, larger):
    if not smaller:
        return True
    window = len(smaller)
    for i in range(len(larger) - window + 1):
        if larger[i:i+window] == smaller:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL
