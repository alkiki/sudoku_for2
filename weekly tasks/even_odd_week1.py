try:
    b = input()
    if float(b).is_integer():
        print('int')
        if int(b) % 2 == 0:
            print('even')
        else:
            print('odd')
except ValueError:
    print('unexpected value')
