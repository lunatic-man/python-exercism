def transform(legacy_data):
    new_value = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            new_value[letter.lower()] = score
    return new_value
