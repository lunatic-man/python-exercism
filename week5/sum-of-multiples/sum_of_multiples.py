def sum_of_multiples(limit, multiples):
    factors = []
    for base in multiples:
        value = base
        while value < limit and value != 0:
            factors.append(value)
            value += base
    factors.sort()
    factors_set = set(factors)
    return sum(factors_set)
