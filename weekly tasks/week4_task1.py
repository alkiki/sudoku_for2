a = list(map(int, input().split()))
res = a[0]
for i in range(1, len(a)):
    res = res * a[i]
print(res)

# var2
# def multiply(nums):
#     result = 1
#     for i in nums:
#         result *= i
#     return result
#
#
# print(multiply([1, 2, 3, 4]))
