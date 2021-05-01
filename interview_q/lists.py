# make a list of your daily schedule 
# something like 'wake up' 600,700, 'eat' 800,900, work, 900,100 .... and so on 
nl = "\n"
routine = ['wake up', 600, 700,
            'eat', 700, 800,
            'work', 900, 1200,
            'eat', 1200, 1300,
            'work', 1300, 1800,
            'eat', 1800, 1900,
            'cool-down', 2000,2100,
            'sleep', 2200, 'nextday']
# TODO: add context to each task 
# print the list
print(f'{nl}')
print(f'My daily routine: {routine}')
print(f'{nl}')

# print the list in a single column 
print("My daily routine in a column")
print("------------------------------")
for i in routine: 
    print(i)
print(f'{nl}')

# extract only the 'work'
# extract only 'nextday'
print(f'What I do at 9am: {routine[6]}')
print(f'The last thing on the list: {routine[23]}')
print(f'{nl}')

# extract only the strings 
print('My list of things to do today')
print('-----------------------------')
for i in routine: 
    if type(i) == str:
        print(i.upper())
print(f'{nl}')

# extract only integers 
print('My times associated with the list')
print('-----------------------------')
for i in routine: 
    if type(i) == int:
        print(i)
print(f'{nl}')