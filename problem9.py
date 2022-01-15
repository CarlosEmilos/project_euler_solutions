'''
a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

we know that:

a = 2mn

b = m^2 - n^2

c = m^2 + n^2

We have two variables that we can change m and n

we have to change m and n such that

a + b + c = 1000

Brute forced it instead, above method might be better though

'''


def is_triplet(a,b,c):
    if a**2 + b**2 == c**2:
        return True


sum_total = 1000
#horrible running time, gets the job done
for a in range(sum_total):
    for b in range(sum_total):
        for c in range(sum_total):
            if a + b + c == sum_total and is_triplet(a,b,c) == True and a < b < c:
                print(a,b,c)
                break
