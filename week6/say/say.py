def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    
    ones = ['zero','one','two','three','four','five','six','seven',
            'eight','nine','ten','eleven','twelve','thirteen','fourteen',
            'fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    
    if number < 20:
        return ones[number]
    elif number < 100:
        remainder = number % 10
        return tens[number // 10] + (('-' + ones[remainder]) if remainder else '')
    elif number < 1000:
        remainder = number % 100
        return ones[number // 100] + ' hundred' + ((' ' + say(remainder)) if remainder else '')
    elif number < 1_000_000:
        remainder = number % 1000
        return say(number // 1000) + ' thousand' + ((' ' + say(remainder)) if remainder else '')
    elif number < 1_000_000_000:
        remainder = number % 1_000_000
        return say(number // 1_000_000) + ' million' + ((' ' + say(remainder)) if remainder else '')
    else:
        remainder = number % 1_000_000_000
        return say(number // 1_000_000_000) + ' billion' + ((' ' + say(remainder)) if remainder else '')     
