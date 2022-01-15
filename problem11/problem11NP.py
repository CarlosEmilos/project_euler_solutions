import numpy as np
import math

with open("problem11/input.txt", "r") as f:
    x = f.read().splitlines()

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


arr = np.array(parse(x))

arrT = np.transpose(arr)

#find diagonal

print(len(np.diagonal(arr)))

#from -10 to 10
diagonals = []
for i in range(-10, 10):
    diagonals.append(np.diagonal(arr, offset = i))

diagonals = np.array(diagonals, dtype=object)
diagonals = diagonals.tolist()

array_prod = []
transpose_prod = []
diagonal_prod = []

#find products of rows
for index, num in enumerate(arr):
    array_prod.append(math.prod(arr[index:index+4]))
#find products of columns
for index, num in enumerate(arrT):
    transpose_prod.append(math.prod(arrT[index:index+4]))

print(diagonals)
'''
#find products of diagonal
for index, num in enumerate(diagonals):
    #print(num)
    diagonal_prod.append(math.prod(diagonals[index:index+4]))
'''


print(np.amax(array_prod))
print(np.amax(transpose_prod))
