def is_valid(isbn):
    """This function tests if a given isbn number is valid or not.

	Parameters:
		isbn(str): The ISBN number that must be tested

	Returns:
		bool: Is the ISBN number valid?"""

    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    isbn_no=[]
    for index, char in enumerate(isbn):
        if char == 'X' and index == len(isbn) -1:
            isbn_no.append(10)
        elif char.isalpha():
            return False
        else:
            isbn_no.append(int(char))
    result=0
    for index, value in enumerate(isbn_no):
        result += value * (10 - index)
    return result % 11 ==0
