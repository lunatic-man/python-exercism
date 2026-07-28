def translate(text):
    if ' ' in text:
        return ' '.join(translate(word) for word in text.split())
    
    vowels = 'aeiou'
    
    if text[0] in vowels or text[:2] in ('xr', 'yt'):
        return text + 'ay'
    
    i = 0
    while i < len(text):
        if text[i] == 'q' and i + 1 < len(text) and text[i+1] == 'u':
            i += 2
            break
        if text[i] in vowels or (text[i] == 'y' and i > 0):
            break
        i += 1
    
    return text[i:] + text[:i] + 'ay'
