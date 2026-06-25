def square(number):
    """This function is used to calculate the number of grains on any one square of the chessboard.

	Parameters:
		number (int): The value of the square on chessboard, must be between 1 and 64.
	Returns:
		int: The number of grains on that square."""
    if number<=64 and number >=1:
        return 2 ** (number-1)
    else:
        raise ValueError('square must be between 1 and 64')


def total():
    """This function calculates the total number of grains present on the chessboard when all the squares are filled

	Parameters:
		none

	Returns:
		int: The total number of grains on chessboard"""

    result = 0
    for i in range(1,65):
        result += square(i)
    return result
