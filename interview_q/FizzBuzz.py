
from make_random_list import make_a_random_list # imported to have some fun
from bubble_up import bubble_up

# rules: counting upward.
# if a number is divisible by 3 you say 'Fizz', if divisible by 5 you say 'buzz', if divisible by 15 you say 'fizzbuzz'
"""SIMPLE SOLUTION"""
def FizzBuzz(num):
    for i in range(num):
        if i == 0:
            pass
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else: 
            print(i)

# call the function with whatever number you want

"""SOLUTION FOR AN ARRAY OF NUMBERS"""
def FizzBuzz(arr):
    for i in arr:
        if i == 0:
            pass
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else: 
            print(i)