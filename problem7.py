import math
import time
def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return n

# Driver function
t0 = time.time()
c = 0 #for counting

newlist = []

for n in range(0,150000):
    if is_prime(n) != False:
        newlist.append(n)
print("Total prime numbers in range :", c)

t1 = time.time()
print("Time required :", t1 - t0)

print(newlist[10000])
