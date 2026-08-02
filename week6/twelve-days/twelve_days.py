ordinals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
            'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

gifts = [
    'a Partridge in a Pear Tree.',
    'two Turtle Doves, ',
    'three French Hens, ',
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, ',
]

def recite(start_verse, end_verse):
    result = []
    for verse in range(start_verse, end_verse + 1):
        verse_gifts = gifts[:verse][::-1]
        if verse > 1:
            verse_gifts[-1] = 'and a Partridge in a Pear Tree.'
        line = f"On the {ordinals[verse-1]} day of Christmas my true love gave to me: {''.join(verse_gifts)}"
        result.append(line)
    return result
