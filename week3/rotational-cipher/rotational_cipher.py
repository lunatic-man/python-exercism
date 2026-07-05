def rotate(text, key):
    """This function gives the output as a string which has been rotated according to a key.

	Parameters:
		text(str): The text which is to be rotated.
		key: the number of positions it must be rotated by.

	Returns:
		str: Rotated Text"""

    new_str = []
    for char in text:
        if char.isupper():
            position = ord(char) - 65
            new_position = (position + key) % 26
            new_str.append(chr(new_position + 65))
        elif char.islower():
            position = ord(char) - 97
            new_position = (position + key) % 26
            new_str.append(chr(new_position + 97))
        else:
            new_str.append(char)
    string = ''.join(new_str)
    return string
