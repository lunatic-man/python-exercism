def append(list1, list2):
    newlist =[]
    i=0
    while i < length(list1):
        newlist += [list1[i]]
        i+=1
    j=0
    while j < length(list2):
        newlist +=[list2[j]]
        j+=1
    return newlist
    
def concat(lists):
    newlist = []
    for ls in lists:
         newlist = append(newlist, ls)
    return newlist


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result


def length(list):
    size = 0
    for i in list:
        size += 1
    return size

def map(function, list):
    newlist = []
    for ls in list:
        newlist += [function(ls)]
    return newlist
    
def foldl(function, list, initial):
    for ls in list:
        initial = function(initial,ls)
    return initial


def foldr(function, list, initial):
    for ls in reverse(list):
        initial = function(initial,ls)
    return initial

def reverse(list):
    newlist = []
    i =  -1
    while i >= -length(list):
        newlist += [list[i]]
        i-=1
    return newlist
