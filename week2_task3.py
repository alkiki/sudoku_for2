a = int(input())
b = int(input())
res = 0
if a >= b:
    while a >= b:
        a = a - b
        res += 1
        if a < b and a != 0:
            print(res, 'remainder:', a)
            exit()
    print(res, 'remainder:', a)
else:
    print('Cannot process the division')
