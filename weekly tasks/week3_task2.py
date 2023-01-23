word = str(input())
result = str()
result2 = list()
res1 = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'z']
for i in range(len(vowels)):
    if word[0] == vowels[i]:
        result = word + 'ay'
for i in range(len(consonants)):
    if word[0] in consonants and word[1] in consonants:
        res1 = 2
i = 0
if res1 == 2:
    while word[i] not in vowels:
        result2.append(word[i])
        i += 1
print(word[len(result2):], *result2, 'ay', sep='')

# var 2
# first_word = 'technique'
# second_word = 'omelet'
# vowel = 'aeiouy'
# 
# 
# def pig_latin(word):
#     end_string = ''
#     if word[0] in vowel:
#         #vowel rules
#         return word + 'yay'
#     else:
#         word_consonant = ''
#         word_end = ''
#         i = 0
#     for letter in word:
#         if letter in vowel:
#             break
# #            letter is a vowel
#         else:
# #            letter is a consonant
#             word_consonant += letter
#         i += 1
#     end_string=word[i:]
#     return end_string + word_consonant + 'ay'
#print(pig_latin(first_word))
