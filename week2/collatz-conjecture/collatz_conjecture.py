def apply_collatz(num):
    """This function returns the result after collatz conjecture has been called once.

	Parameter:
		num(int): The number which must be tested for odd or even and operated on
	Returns:
		int: The result after one operation"""
    if num % 2 ==0:
        return num // 2
    else:
        return (num * 3) +1

def steps(number):
    """This function returns the number of steps it takes for a number to reach 1 following Collatz Conejcture.

	Parameters:
		number (int): Must an integer greater than or equal to 1
	Returns:
		int: The number of steps it takes to reach 1"""
    if number<1:
        raise ValueError("Only positive integers are allowed")


    step_count=0
    while(number!=1):
        number = apply_collatz(number)
        step_count+=1
    return step_count
