def equilateral(sides):
    """Parameters:
        sides (list[int]): Takes three integer values

	   Returns:
	   bool: is the triangle equilateral?

	This function tests for equilateral triangles."""

    for i in range(-3,0):
        if sides[i] + sides[i+1] <= sides[i+2]:
            return False

    if sides[0] == sides[1] == sides[2]:
        return True
    else:
        return False

def isosceles(sides):
    """Parameters:
	   sides (list[int]): Takes three integer values

	   Returns:
	   bool: is the triangle isoceles?

	This function tests for isosceles triangles."""


    for i in range(-3,0):
        if sides[i] + sides[i+1] <= sides[i+2]:
            return False

    if sides[0]==sides[1] or sides[1]==sides[2] or sides[2]==sides[0]:
        return True
    else:
        return False

def scalene(sides):
    """Parameters:
           sides (list[int]): Takes three integer values

           Returns:
           bool: is the triangle scalene?

        This function tests for scalene triangles."""

    for i in range(-3,0):
        if sides[i] + sides[i+1] <= sides[i+2]:
            return False

    return sides[0]!=sides[1] and sides[1]!=sides[2] and sides[2]!=sides[0]
