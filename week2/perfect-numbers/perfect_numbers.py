def get_factors(number):
    """This function returns the list of all the factors of a number.

	Parameters:
		number (int): A positive integer
	Returns:
		list (int): List of all factors of this number"""

    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    elif number==1:
        ls = []
        return ls
    else:
        ls =[1]
        for i in range(2,number):
            if number % i == 0:
                ls.append(i)
        return ls


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    	Parameters:
		number (int): a positive integer
	Returns:
		str: Is the number Perfect, Adundant or Deficient?
    """
    result = sum(get_factors(number))
    if result == number:
        return 'perfect'
    elif result > number:
        return 'abundant'
    else:
        return 'deficient'
