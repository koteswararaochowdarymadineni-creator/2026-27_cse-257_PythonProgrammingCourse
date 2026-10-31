
# Employee Payroll and Deduction Analysis

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic = float(input("Enter Basic Salary: "))
allowances = float(input("Enter Allowances: "))
overtime_hours = float(input("Enter Overtime Hours: "))
overtime_rate = float(input("Enter Overtime Rate: "))
incentives = float(input("Enter Incentives: "))

overtime_pay = overtime_hours * overtime_rate

gross_salary = basic + allowances + overtime_pay + incentives

if gross_salary <= 20000:
    deduction = gross_salary * 0.05

elif gross_salary <= 40000:
    deduction = 1000 + (gross_salary - 20000) * 0.10

else:
    deduction = 3000 + (gross_salary - 40000) * 0.15

net_salary = gross_salary - deduction
print("\n====================================")
print("          SALARY STATEMENT")
print("====================================")
print("Employee Name     :", name)
print("Employee ID       :", emp_id)
print("------------------------------------")
print("Basic Salary      : Rs.", basic)
print("Allowances        : Rs.", allowances)
print("Overtime Pay      : Rs.", overtime_pay)
print("Incentives        : Rs.", incentives)
print("------------------------------------")
print("Gross Salary      : Rs.", gross_salary)
print("Total Deduction   : Rs.", deduction)
print("------------------------------------")
print("Net Salary        : Rs.", net_salary)
print("====================================")

