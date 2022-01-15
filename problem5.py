import math

twenties = [i*(19*20) for i in range(1,1000000)]
nums = [3,6,7,8,9,11,12,13,14,15,16,17,18,19]
#print(len(nums))
k = 0

for i in twenties:
    k = 0
    for j in nums:
        if i % j == 0:
            k += 1
            if k == 14:
                print(i)
