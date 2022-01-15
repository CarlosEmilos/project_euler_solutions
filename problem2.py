'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''
#find even fibbonachi numbers, simple approach
def EvenFib(n):
    fibs = [0,1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

#get the first 100 (i just assumed that the first 100 would never exceed 4 mil)
fibnums = EvenFib(100)
newlist = []
#check if each number is even and does not exceed 4 mil
for i in fibnums:
    if i % 2 == 0 and i <= 4000000:
        newlist.append(i)

#get sum of newlist
print(sum(newlist))
