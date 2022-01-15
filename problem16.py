'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''

num = 2**1000

num = str(num)
newlist = []
for i in num:
    newlist.append(int(i))

print(sum(newlist))
