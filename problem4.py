#gonna use itertools:

from itertools import permutations

'''
Smallest product of two 3-digit numbers would be 111*111 = 12321
The largest would be  999*999 = 998001

steps are:

1. create list of all numbers from between 12321 and 998001

2. find all palindromes in them

3. hope to God that it's a product of two three digit numbers LOL

3.1 apparently thats not correct
'''
nums = [i for i in range(12321, 998001)]

#print(nums[0:10])

palindromes = []

for i in nums:
    i = str(i)

    if i == i[::-1]:
        palindromes.append(i)

print(palindromes[-2])


#test

def getFactors(n):
    newlist = [1,n]
    #for a number to be a factor, it must devide evenly into the number
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            newlist.append(i)
    return newlist

for i in palindromes[-100:-50]:
    i = int(i)
    print(getFactors(i))
