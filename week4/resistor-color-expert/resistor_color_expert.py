mapping = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
tolerance = {"grey": "0.05%", "violet":"0.1%", "blue":"0.25%", "green":"0.5%", "brown":"1%", "red":"2%", "gold":"5%", "silver":"10%"}

def resistor_label(colors):
    """Function to return value in string foramt with proper metric prefixes.

	Parameters:
		colors (list): list of colors on resistor

	Returns:
		str: Numerical value with correct metric prefix"""

    symbol = chr(177)
    if len(colors) == 5:
        result = (mapping[colors[0]]*100 + mapping[colors[1]]*10 + mapping[colors[2]]) * 10**mapping[colors[3]]
        if result%pow(10,9) == 0 and result !=0:
            return str(result // 10**9) + " gigaohms " +symbol+tolerance[colors[4]]
        elif result%pow(10, 6) == 0 and result !=0:
            if result < 1000:
                return str(result // pow(10,6)) + " megaohms " +symbol+tolerance[colors[4]]
            else:
                return str(result / 10**9) + " gigaohms "+symbol+tolerance[colors[4]]
        elif result%pow(10, 3) == 0 and result !=0:
            if result < 1000:
                return str(result // pow(10,3)) + " kiloohms " +symbol+tolerance[colors[4]]
            else:
                return str(result / 10**6) + " megaohms "+symbol+tolerance[colors[4]]
        else:
            if result < 1000:
                return str(result) + " ohms " +symbol+ tolerance[colors[4]]
            else:
                return str(result / 10**3) + " kiloohms "+symbol+tolerance[colors[4]]

    elif len(colors) == 4:
        result = (mapping[colors[0]]*10 + mapping[colors[1]]) * pow(10, mapping[colors[2]])
        if result%pow(10,9) == 0 and result !=0:
            return str(result // 10**9) + " gigaohms " +symbol+tolerance[colors[3]]
        elif result%pow(10, 6) == 0 and result !=0:
            return str(result // pow(10,6)) + " megaohms " +symbol+tolerance[colors[3]]
        elif result%pow(10, 3) == 0 and result !=0:
            return str(result // pow(10,3)) + " kiloohms " +symbol+tolerance[colors[3]]
        else:
            if result < 1000:
                return str(result) + " ohms " +symbol+ tolerance[colors[3]]
            else:
                return str(result / 10**3) + " kiloohms "+symbol+tolerance[colors[3]]
    else:
        return str(mapping[colors[0]]) + " ohms"
