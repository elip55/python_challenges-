
# CHALLENGE:  Create a graph of the first five cubes numbers 

import matplotlib.pyplot as plt
import numpy as np
import math

first_numbers = [1,2,3,4,5]

def find_cubes():
    first_cubes = []
    for num in first_numbers:
        newnum = pow(num, 3)
        if newnum not in first_cubes:
            first_cubes.append(newnum)
    return first_cubes

cubes = find_cubes()
plt.style.use('seaborn')
fig, l = plt.subplots()
l.scatter(first_numbers, cubes)
l.set_title('Square Numbers', fontsize = 25)
l.set_xlabel('Values', fontsize = 18)
l.set_ylabel('Cubed', fontsize = 18)
l.tick_params(axis = 'both', labelsize = 18)
plt.show()