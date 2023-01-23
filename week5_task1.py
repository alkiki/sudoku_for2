nato = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'xray',
    'z': 'zulu',
}


def nato_to_word(sentence):
    for word in sentence.split(' '):
        for key, value in nato.items():
            if value == word:
                print(key)


nato_to_word('charlie alpha tango')


def word_to_nato(word):
    result = ''
    for letter in word:
        result += nato[letter] + ' '
    print(result)


word_to_nato('cat')
