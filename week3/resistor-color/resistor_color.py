mapping = {'black':'0', 'brown':'1', 'red':'2', 'orange':'3', 'yellow':'4', 'green':'5', 'blue':'6', 'violet': '7', 'grey':'8', 'white':'9'}
def color_code(color):
    """This function is used to return the numerical value of a particular color passed to it.

	Parameters:
		color(str): The color whose value is to be found, acts as key.
	Returns:
		int: The numeric value of color"""

    return int(mapping[color])


def colors():
    """This function returns the list of all the different band colors.

	Parameters:
		null

	Returns:
		list: List of all valid band colors"""

    return [index for index in mapping.keys()]
