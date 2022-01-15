import math

'''
What is the greatest product of four adjacent
numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''

with open("problem11/input.txt", "r") as f:
    x = f.read().splitlines()


'''
1. find largest product of 4 adjacent numbers for all in the right direction

2. find largest product of 4 adjacent numbers for all in the down direction

'''

def parse(x):
    #returns a list of lists
    newlist = []
    for i, strings in enumerate(x):
        strings = strings.split()
        #create a new list in our list
        newlist.append([])
        for j in strings:
            newlist[i].append(int(j))
    return newlist
'''
def rightProd(x):
    rights = []
    for lists in x:
        print(lists)
        for index, num in enumerate(lists):
            rights.append(math.prod(lists[index:index+4]))
    return rights
'''
def rightProd(x):
    length_of_prod = 4
    current = 1
    largest_so_far = 0
    #outer list
    for i in range(len(x)):
        #inner list
        #note "- length of prod" or else it will exceed bounds
        for j in range(len(x[i])-length_of_prod):
            #from current element and 4 steps ahead
            for k in range(length_of_prod):
                #just like += but with product
                current *= x[i][j+k]
                #print(current)
            #check if current is larger
            if current > largest_so_far:
                #assign value"
                largest_so_far = current
            #reset current
            current = 1
    return largest_so_far

def downProd(x):
    length_of_prod = 4
    current = 1
    largest_so_far = 0
    #length of product going on the vertical axis now
    for i in range(len(x)-length_of_prod):
        for j in range(len(x[i])):
            for k in range(length_of_prod):
                #change the index to look at
                #looking "down" instead of right
                current *= x[i+k][j]
            if current > largest_so_far:
                largest_so_far = current
            current = 1
    return largest_so_far

def rightDiagonalProd(x):
    length_of_prod = 4
    current = 1
    largest_so_far = 0
    #length of product going on BOTH  axis now
    for i in range(len(x)-length_of_prod):
        for j in range(len(x[i])-length_of_prod):
            for k in range(length_of_prod):
                #change the index to look at
                #looking "down" instead of right
                current *= x[i+k][j+k]
            if current > largest_so_far:
                largest_so_far = current
            current = 1
    return largest_so_far

def leftDiagonalProd(x):
    length_of_prod = 4
    current = 1
    largest_so_far = 0
    #length of product going on BOTH  axis now
    for i in range(len(x) - length_of_prod):
        for j in range(length_of_prod, len(x[i])):
            for k in range(length_of_prod):
                #change the index to look at
                #looking "down" instead of right
                current *= x[i+k][j-k]
            if current > largest_so_far:
                largest_so_far = current
            current = 1
    return largest_so_far





print(rightProd(parse(x)))
print(downProd(parse(x)))
print(rightDiagonalProd(parse(x)))
print(leftDiagonalProd(parse(x)))
