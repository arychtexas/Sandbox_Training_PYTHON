# Lets calculate a annual Salary

wages = int(input("Please Enter hourly wage rate:$" ))
hours = int(input("Please Enter hours you worked per day: " ))
days_worked = int(input("Please Enter days worked this year: "))
salary = float(wages*hours*days_worked)
print(f"Your annual salary is ${salary}")

# Lets add a raise 

raise_salary = int(input("Enter in desired raise precentage. Use whole number:  "))
print(f"Your new annual salary is ${salary*(raise_salary/100)+salary}")