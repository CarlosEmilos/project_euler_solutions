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

insane runtime, 0,144 seconds vs slow solution which is
'''

def is_triplet(a,b,c):
    if a**2 + b**2 == c**2:
        return True

def find_triplet_sum(target):
    for m in range(target):
        for n in range(target):
            a = 2*m*n
            b = m**2 - n**2
            c = m**2 + n**2
            #pretty sure the is_triplet function dosnt matter since the above
            #calculations make sure that it's a triplet every time
            #if a + b + c == target and is_triplet(a,b,c) and a < b < c:
            if a + b + c == target and a < b < c:
                return a,b,c
                break
print(find_triplet_sum(1000))
