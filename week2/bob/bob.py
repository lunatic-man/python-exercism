def response(hey_bob):
    """This function gives the statement said by Bob when a particular type of statement is told to him.

	Parameters:
		hey_bob (str): The statement which is told to Bob
	Returns:
		str: Based on the statement, different statements are returned"""
    response = hey_bob.strip()
    is_question = response.endswith('?')
    is_yelling = response.isupper()
    if not response:
        return 'Fine. Be that way!'
    elif is_question and not is_yelling:
        return 'Sure.'
    elif is_yelling and not is_question:
        return 'Whoa, chill out!'
    elif is_yelling and is_question:
        return 'Calm down, I know what I\'m doing!'
    else:
        return 'Whatever.'
