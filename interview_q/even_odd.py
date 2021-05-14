# print even and odd numbers in range 100


values = range(1,100)
def even():
    for i in values: 
        if i % 2 == 0: 
            print(i)
def odd():
    for i in values:
        if i % 2 != 0:
            print(i)
print("EVEN")        
even()
print("-----------------------")
print("ODD")
odd()