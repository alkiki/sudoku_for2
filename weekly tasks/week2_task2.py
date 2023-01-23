phrase = str(input())
b = list(map(chr, range(97, 123)))
for i in b:
    for y in phrase:
        if i == y:
            for x in b:
                print(x, ':', phrase.count(x))
        break

#  var 2
# sentence = str(input())
# alphabets ="abcdefghijklmnopqrstuvwxyz . , "
# 
# for i in alphabets:
#     count = 0
#     for j in sentence:
#         if j.lower() == i:
#             count += 1
#     print(i, ": ", count)
