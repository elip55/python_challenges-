# create a basic program to convert hourly pay to yearly pay 

def calculations(pay,hours):
    yearly_salary = (pay*hours)*52
    print(yearly_salary)

try:
    pay = float(input("How much do you get paid an hour? "))
except:
    print("ERROR:  PLEASE ENTER THE AMOUNT IN DOLLARS AND CENTS!\nPLEASE RUN THE PROGRAM AGAIN!")
    exit()
try:
    hours = float(input("How many hours do you work per week? "))
except:
    print("ERROR:  PLEASE ENTER THE EXACT AMOUNT OF HOURS.\nPLEASE RUN THE PROGRAM AGAIN")
    exit()
calculations(pay,hours)