# name = str(input())
# surname = str(input())
# print('Hello there, ', name, ' ', surname, '!', sep='')
def greeting(name, family_name=''):
    if family_name=='':
        print('Hello, ' + name)
    else:
        print('Hello, ' + name + family_name)


greeting('Alina', ' Yagafarova')
