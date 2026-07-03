def is_isogram(phrase):
    """This exercise is used to check if a phrase is an isogram or not (no repeated letters).

	Parameters:
		phrase(str): the phrase that is to be tested

	Returns:
		bool: Is the phrase an isogram?"""

    new_str = ''.join(char for char in phrase.lower() if char.isalpha())
    test = set(new_str)
    return len(test) == len(new_str)
