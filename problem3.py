

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
#see if number is factor
def getFactors(n):
    newlist = [1,n]
    #for a number to be a factor, it must devide evenly into the number
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            newlist.append(i)
    return newlist

print(getFactors(6))


#see if number is prime
def isPrime(n):
    if len(getFactors(n)) == 2:
        return n

#get primeFactors of newlist
primeFactors = getFactors(600851475143)

newlist = []

for i in primeFactors:
    newlist.append(isPrime(i))

print(newlist)

#print("hello world")
