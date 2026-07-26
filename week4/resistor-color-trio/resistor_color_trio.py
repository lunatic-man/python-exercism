mapping = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
def label(colors):
    """Function to return value in string foramt with proper metric prefixes.

	Parameters:
		colors (list): list of colors on resistor

	Returns:
		str: Numerical value with correct metric prefix"""

    result = (mapping[colors[0]]*10 + mapping[colors[1]]) * pow(10, mapping[colors[2]])
    if result%pow(10,9) == 0 and result !=0:
        return str(result// pow(10,9)) + " gigaohms"
    elif result%pow(10, 6) == 0 and result !=0:
        return str(result // pow(10,6)) + " megaohms"
    elif result%pow(10, 3) == 0 and result !=0:
        return str(result // pow(10,3)) + " kiloohms"
    else:
        return str(result) + " ohms"
