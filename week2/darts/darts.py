def distance(x,y):
    """This function calculates of the given points (x,y) from the center using the distance formula
	Parameters:
		x (int): Distance of the point from Y axis
		y (int): Distance of the point from X Axis

	Returns:
		float: Distance from the center"""

    return (x ** 2 + y ** 2) ** 0.5



def score(x, y):
    """This function calculates the points scored in one throw of the dart.

	Parameters:
		x (int): Distance from the Y Axis
		y (int): Distance from the X Axis

	Returns:
		int: Points score in that throw"""
    d = distance(x,y)
    if d>10:
        return 0
    elif d>5:
        return 1
    elif d>1:
        return 5
    else:
        return 10 
