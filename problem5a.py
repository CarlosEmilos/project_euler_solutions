tens = [i*10 for i in range(1,300)]
nums = [3,4,6,7,8,9]


#print(tens)
'''
for i in tens:
    k = 0
    for j in nums:
        if k == 6:
            print("Answer is ", i)
            break
        elif i % j == 0:
            k += 1
'''

for i in tens:
    k = 0
    for j in nums:
        if i % j == 0:
            k += 1
            if k == 6:
                print(i)
        elif k == 6:
            print("Answer is ", i)
            break
