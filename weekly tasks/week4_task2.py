words = ['comfortable', 'round', 'support', 'machinery']


def random(words):
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] == words[j]:
                continue
            print(words[i], '', words[j])


random(words)
