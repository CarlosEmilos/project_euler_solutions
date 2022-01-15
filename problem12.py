import math

'''
Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

nth triangular number is the sum of first n natural numbers  =  n(n+1)/2
'''

'''
functions:

a fuction to give me triangluar numbers

a function to get me the divisors of the number

run untill you get 500 diviors

a bit too much guess work, and not super efficient, took 12 seconds for code to finish.

'''

def nTriangle(n):
        #return int(n*(n+1)/2)
        newlist = []
        for i in range(1,n+1):
            newlist.append(int(i*(i+1)/(2)))

        return newlist

def printDivisors(n):
    newlist = []
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0) :

            # If divisors are equal, print only one
            if (n / i == i):
                newlist.append(i),
            else:
                # Otherwise print both
                newlist.append(i)
                newlist.append(n//i)
        i = i + 1
    #newlist.remove()
    newlist = sorted(newlist)
    return newlist[:-1]

#print(printDivisors(nTriangle(28)))

for i in nTriangle(100000):
    if len(printDivisors(i)) >= 500:
        print(i)
        break
