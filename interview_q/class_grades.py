# creat a list of the grades in the class 
# display the highest grade, lowest grade, and the average

grades = [66.00 , 65.50, 79.00, 80.98, 54.55, 99.89, 87.77, 91.12, 79.98, 81.19, 100.00, 100.11, 34.109, 102.339]
grades_sum = sum(grades)
amount_grades = len(grades)

high_counter = 0
low_counter = 110 

for number in grades: 
    if number > high_counter:
        high_counter = round(number,2)
        
print(f'The highest grade is: {high_counter}')
print(f'The lowest grade is: {round(min(grades),2)}')

average = round((grades_sum/amount_grades),2)
print(f'The average grade was: {average}')