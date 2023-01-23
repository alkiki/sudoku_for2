import Levenshtein
text = open('cyberspace_original.txt')
dictionary_file = open('dictionary.txt')
dictionary = dictionary_file.readlines()
lines = text.readlines()

for index, word in enumerate(dictionary):
    dictionary[index] = word.strip()

split_lines = []

for line in lines:
    split_lines.append(line.split(' '))

for line in split_lines:
    for i, word in enumerate(line):
        if word.lower().strip() in dictionary or word == '\n':
            line[i] = word
        else:
            minimum = 3
            correct_word = word
            for dict_word in dictionary:
                final_distance = Levenshtein.distance(word.lower(), dict_word)
                if minimum > final_distance:
                    minimum = final_distance
                    correct_word = dict_word
            print(str(minimum) + ' ' + correct_word)
            line[i] = correct_word

join_lines = []
for split in split_lines:
    join_lines.append(''.join(split))

with open('corrected.txt', 'w') as file:
    file.write(''.join(split_lines))

# print(''.join(split_lines))
