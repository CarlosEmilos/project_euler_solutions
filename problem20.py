'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
#make a list of numbers from 1,100
nums = [i for i in range(1,101)]

#make a factorial function
def factorial(x):
    product = 1
    for i in x:
        product *= i
    return product

#find the factorial of 100
number = str(factorial(nums))

#find sum of numbs in that number
def sum(x):
    sum = 0
    for i in x:
        i = int(i)
        sum += i
    return sum

#number = "1234"

print(sum(number))
