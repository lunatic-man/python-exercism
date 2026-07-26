mapping = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
def value(colors):
    """Function to get value of first two colors.

	Parameters:
		colors (list): list of all colors possible
	Returns:
		int: two digit number showing value of colors"""

    return (mapping[colors[0]]*10 + mapping[colors[1]])
