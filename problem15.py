import scipy.special

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?


According to wikipedia,

formula is: print(scipy.special.binom(2*n, n))

'''

print(scipy.special.binom(2*20, 20))
