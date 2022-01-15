'''
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def fizzBuzz(x):
    '''
    Returns a list of multiples between 1 and x
    '''
    newlist = []

    for i in range(1,x):
        if i % 3 == 0:
            newlist.append(i)
        elif i % 5 == 0:
            newlist.append(i)
        else:
            continue
    return newlist


print(sum(fizzBuzz(1000)))
