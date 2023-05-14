# print even and odd numbers in any range

def even_odd(arr):
    for i in arr:
        if i % 2 == 0:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')

l = []
for i in range(100):
    l.append(i)


even_odd(l)