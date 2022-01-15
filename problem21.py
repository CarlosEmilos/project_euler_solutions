
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
def proper_divs(n):
    '''
    Finds proper diviors
    '''
    newlist = []
    for x in range(1,n+1//2):
        if(n % x == 0):
            newlist.append(x)
    return newlist

#print(proper_divs(10000000))

def amicable_nums(x):
    '''
    finds all amicable numbers under x
    '''
    first_an = sum(proper_divs(x))
    second_an = sum(proper_divs(first_an))

    if x == second_an and second_an != first_an:
        return first_an


#about 6 seconds
amic = []
for i in range(220, 10000):
    if amicable_nums(i) != None:
        amic.append(amicable_nums(i))

print(amic)
print(sum(amic))
