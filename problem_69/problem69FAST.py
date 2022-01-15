
'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine
the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

NOTE: you need to find the greatest value for n/phi(n)

How to optimize the code?

Maybe make a check for prime numbers at the start of the function as well?
Since phi(p) = p-1

'''
import math
import sympy as sp


#combines functionality of the primeDivisor function
def calcPhi(n):
    newlist = []
    #prod = 1
    #goes through all divisors
    if sp.ntheory.isprime(n) == True:
        newlist.append(n)
    else:
        for i in sp.divisors(n):
            #checks if it's prime (therefore, prime divisor)
            if sp.ntheory.isprime(i) == True:
                #appends to a lxxist according to the formula above
                newlist.append(1-(1/i))
    prod = n*math.prod(newlist)
    return prod


largest_so_far = 1
start_num = 0
#gonna try with the first 10
for i in range(1, 11):
    if i/calcPhi(i) > largest_so_far:
        largest_so_far = i/calcPhi(i)
        start_num = i
    else:
        continue
print(largest_so_far)
print(start_num)

#runtime = 1,054s
#optimization is negligeble
