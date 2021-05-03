
# create the famed Fibonacci sequence with 10 terms
# terms should be 0,1,1,2,3,5,8,13,21,34
# Fn = Fn-1 + Fn-2
# Python program to display the Fibonacci sequence

def f(x):
    if x <= 1:
        return x # return the values 0,1 
    else:
        equation = f(x-1)+f(x-2) # add fibonacci equation with function values to return values past the first two terms
        return equation
    
for i in range(10): # loop over whatever range necessary 
    print(f(i))