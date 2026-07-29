import string
ls = string.ascii_lowercase
revLs = string.ascii_lowercase[-1::-1]
mapping = dict.fromkeys(ls, 'a')
for i,key in enumerate(mapping):
    mapping[key] = revLs[i]
    
def encode(plain_text):
    plain_text = plain_text.lower()
    encoded = []
    count = 0
    for char in plain_text:
        if char in mapping:
            if count > 0 and count % 5 == 0:
                encoded.append(' ')
            encoded.append(mapping[char])
            count += 1
        elif char.isdigit():
            if count > 0 and count % 5 == 0:
                encoded.append(' ')
            encoded.append(char)
            count += 1
    encodedStr = ''.join(encoded).strip()
    return encodedStr

def decode(ciphered_text):
    plain = []
    for char in ciphered_text:
        if char in mapping:
            plain.append(mapping[char])
        elif char.isdigit():
            plain.append(char)
    return ''.join(plain)
