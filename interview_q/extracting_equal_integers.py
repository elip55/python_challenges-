# 1: Extract equal integers from a list and make a new list of no repeating numbers 
# 2: Write a .txt document using those numbers 
# 3: Add a header in the .txt document 

oldlist = [1,2,3,4,4,5,5,6]
newlist = []
mystring = ""
samestring = "This is the"
header = 'Arranged list without repeating values: \n'

for i in range(len(oldlist)): 
    if i == oldlist.index(oldlist[i]):
        if oldlist[i] not in newlist:
            newlist.append(oldlist[i])
tablerows = f'{newlist[0]} {samestring} first row.\n{newlist[1]} {samestring} second row .\n{newlist[2]} {samestring} third row.\n{newlist[3]} {samestring} fourth row .\n{newlist[4]} {samestring} fifth row.\n{newlist[5]} {samestring} final row.'
w = open('non_repeating.txt', 'w')
w.write(header)
w.write(tablerows)
w.close()
