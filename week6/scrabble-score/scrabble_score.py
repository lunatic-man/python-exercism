mapping = {
    1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2:['D', 'G'],
    3:['B', 'C', 'M', 'P'],
    4:['F', 'H', 'V', 'W', 'Y'],
    5:['K'],
    8:['J', 'X'],
    10:['Q', 'Z']
}



def score(word):
    final_score = 0
    word = word.upper()
    for letter in word:
        for score, collection in mapping.items():
            if letter in collection:
                final_score += score
                break            
    return final_score
