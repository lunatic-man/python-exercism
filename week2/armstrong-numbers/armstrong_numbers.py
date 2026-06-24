def is_armstrong_number(number):
    """This function is used to test if a number is an Armstrong Number or not. Armstrong Logic: Sum of each digit raised to the power of
    the number of digits should be equal to the original number.
	Parameters:
		number (int): The number that need to be tested.
	Returns:
		bool: Is the number armstrong?
    """

    org_number = number
    result = 0
    length = len(str(number))
    while (number != 0):
         result += (number % 10) ** length
         number = number // 10
    return result == org_number
