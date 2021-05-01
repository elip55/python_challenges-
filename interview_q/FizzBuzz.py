

# rules: counting upward.
# if a number is divisible by 3 you say 'Fizz', if divisible by 5 you say 'buzz', if divisible by 15 you say 'fizzbuzz'

num = range(1,100)
for i in num:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else: 
        print(i)