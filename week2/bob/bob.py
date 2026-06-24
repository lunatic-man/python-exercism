def response(hey_bob):
    response = hey_bob.strip()
    if not response:
        return 'Fine. Be that way!'
    elif response[-1] == '?' and not response.isupper():
        return 'Sure.'
    elif response.isupper() and response[-1] != '?':
        return 'Whoa, chill out!'
    elif response.isupper() and response[-1] == '?':
        return 'Calm down, I know what I\'m doing!'
    else:
        return 'Whatever.'
