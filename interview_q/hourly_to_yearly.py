# create a basic program to convert hourly pay to yearly pay 

def calculations(pay,hours):
    yearly_salary = (pay*hours)*52
    print(yearly_salary)


pay = float(input("How much do you get paid an hour?"))
hours = float(input("How many hours do you work per week?"))
calculations(pay,hours)