# use a dictionary to print 3 major rivers and the country it runs through 
# print contries first
# print rivers second
# print statement third

statement = ""
rivers = {'egypt':'nile', 'USA':'mississippi', 'republic of congo':'congo'}
print('\n')
for i in rivers:
    print(i.title())
print('---------------')
for i in rivers.values():
    print(i.title())
print('---------------')
for key,value in rivers.items():
    statement += f'The {value.title()} runs through: {key.title()}.\n'

print(statement)