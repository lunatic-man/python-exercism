EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return (EXPECTED_BAKE_TIME - elapsed_bake_time)


def preparation_time_in_minutes(layers):
	"""Calculate time need for preparation

	Parameters:
		layers (int): The number of layers in lasagna

	Returns:
		int: The total prep time needed (in minutes) assuming each layer takes 2 mins to prepare

	Function takes layers as input and returns the time needed in minutes to prepare lasagna before putting in oven.
	"""

	return (layers * PREPARATION_TIME)

def elapsed_time_in_minutes(layers, elapsed_bake_time):
	"""Calculates how much time has already been spent in preparation of Lasagna

	Parameters:
		elapsed_bake_time (int): The amount of time in minutes already spent in oven
		layers (int): The number of layers the Lasagna has

	Returns:
		int: The amount of time spent in preparation

	Function returns the total time spent in making Lasagna by using time for layer prep
	and using time already spent in oven.

	"""
	return (elapsed_bake_time + (layers * PREPARATION_TIME))



