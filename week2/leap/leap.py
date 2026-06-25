def leap_year(year):
    """This function is used to check if the input value is a leap year or not.

	Parameters:
		year (int): The year which you want to check in int

	Returns:
		bool: Was the year leap?
	"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
