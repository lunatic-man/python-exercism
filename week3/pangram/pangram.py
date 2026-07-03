import string



def is_pangram(sentence):
    """This function is used to check if a string is a pangram or not.

	Parameters:
		sentence(str): The sentence that is to be tested.
	Returns:
		bool: Is the sentence a pangram?"""
    new_str = sentence.lower()
    return all(letter in new_str for letter in string.ascii_lowercase)
