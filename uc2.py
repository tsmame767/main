#daily employee wage
def calWage(wage,time):
    return f"Employees Daily Wage is {wage*time}"


a=int(input("enter hourly wage of the employee :"))
b=int(input("enter employees total hours a day :"))
print(calWage(a,b))