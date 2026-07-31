def factors(value):
    prime_factors=[]
    i=2
    while value!=0:
        if value==1:
            return prime_factors
        elif value%i==0:
            prime_factors.append(i)
            value//=i
        else:
            i+=1
    return prime_factors
