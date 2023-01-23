# task1
a = int(input())
b = int(input())
c = int(input())
sum1 = 0
if a > b:
    temp = a
    a = b
    b = temp
for i in range(a, b): # if we want to include the last number then range(a, b + 1)
    if i >= c:
        if i % c == 0:
            sum1 += i
print(sum1)

    
