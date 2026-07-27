def flatten(iterable):
    final=[]
    for i in iterable:
        if i is None:
            continue
        elif isinstance(i, list):
            final.extend(flatten(i))
        else:
            final.append(i)
    return final
