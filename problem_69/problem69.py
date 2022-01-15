
'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine
the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

NOTE: you need to find the greatest value for n/phi(n)

Optimizations:

1.If n is prime, then phi(n) = n - 1 (so you shold use a isPrime() function)

2.If n^p is a prime power, then phi(n^p) = n^p - n^(p-1)
example: phi(32) is the same as 2**5, so phi(32) = 2**5 - 2**4 = 16

3. if gcd(m,n) = 1, then phi(m*n) = phi(m)*phi(n)
so if m and n are coprime you can calculate their phi
by multiplying their individual phis together, not sure how to
implement this though


if you have a hard time implementing the above, there is a formula:

If we have all the prime divisors of n, p1, p2 and pn
we can calculate phi(n) like so:

phi(n) = n*(1-(1/p1))*(1-(1/p2))...*(1-(1/pn))

example:
The only prime divisors of 600 are 2,3 and 5, so:

phi(600) = 600*(1-(1/2)) * (1-1/3) * (1-1/5) = 160

Note that I've already made primenumber and divisor methods, so I've used sympy
for this one

'''
import math
import sympy as sp


#combines functionality of the primeDivisor function
def calcPhi(n):
    newlist = []
    prod = 1
    #goes through all divisors
    for i in sp.divisors(n):
        #checks if it's prime (therefore, prime divisor)
        if sp.ntheory.isprime(i) == True:
            #appends to a lxxist according to the formula above
            newlist.append(1-(1/i))
    #calculates the formula
    for i in newlist:
        prod *= i
    return int(n*prod)


largest_so_far = 1
start_num = 0

for i in range(1, 11):
    if i/calcPhi(i) > largest_so_far:
        largest_so_far = i/calcPhi(i)
        start_num = i
    else:
        continue
print(largest_so_far)
print(start_num)

#runtime is 1,1455
