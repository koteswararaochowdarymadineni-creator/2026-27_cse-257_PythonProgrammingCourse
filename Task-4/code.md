

# Employee Payroll and Deduction Analysis

## 1. Problem Statement

Write a Python program to calculate an employee's gross salary using basic pay, allowances, overtime pay, and incentives. Apply progressive deductions based on the gross salary and calculate the net salary. Finally, generate a formatted salary statement showing all earnings, deductions, gross salary, and net salary.

## 2. Algorithm

1. Start the program.
2. Read employee name and employee ID.
3. Read basic salary, allowances, overtime hours, overtime rate, and incentives.
4. Calculate overtime pay.

`Overtime Pay = Overtime Hours × Overtime Rate`

5\. Calculate gross salary.

`Gross Salary = Basic Salary + Allowances + Overtime Pay + Incentives`

6. Calculate progressive deductions:
   - If gross salary is up to ₹20,000, deduction is 5%.
   - If gross salary is between ₹20,001 and ₹40,000, deduction is 10% on the amount above ₹20,000, plus ₹1,000.
   - If gross salary is above ₹40,000, deduction is 15% on the amount above ₹40,000, plus ₹3,000.
7. Calculate net salary.

`Net Salary = Gross Salary - Total Deduction`

8. Display the formatted salary statement.
9. Stop the program.

## 3. Input – Process – Output (IPO)

| Input          | Process                      | Output           |
| -------------- | ---------------------------- | ---------------- |
| Employee name  | Calculate overtime pay       | Employee details |
| Employee ID    | Calculate gross salary       | Gross salary     |
| Basic salary   | Apply progressive deductions | Total deductions |
| Allowances     | Calculate net salary         | Net salary       |
| Overtime hours | Format salary statement      | Salary statement |
| Overtime rate  |                              |                  |
| Incentives     |                              |                  |

## 4. Flowchart
```mermaid

flowchart TD
    A([START]) --> B[/Enter Employee Name and Employee ID/]

    B --> C[/Enter Basic Salary/]
    C --> D[/Enter Allowances/]
    D --> E[/Enter Overtime Hours and Overtime Rate/]
    E --> F[/Enter Incentives/]

    F --> G[Calculate Overtime Pay]
    G --> H[Overtime Pay = Hours * Rate]

    H --> I[Calculate Gross Salary]
    I --> J[Gross = Basic + Allowances + Overtime Pay + Incentives]

    J --> K{Gross Salary <= 20000?}

    K -- YES --> L[Deduction = Gross Salary * 5%]

    K -- NO --> M{Gross Salary <= 40000?}

    M -- YES --> N[Deduction = 1000 + (Gross - 20000) * 10%]

    M -- NO --> O[Deduction = 3000 + (Gross - 40000) * 15%]

    L --> P[Calculate Net Salary]
    N --> P
    O --> P

    P --> Q[Net Salary = Gross Salary - Deduction]

    Q --> R[/Display Employee Details/]
    R --> S[/Display Basic Salary and Allowances/]
    S --> T[/Display Overtime Pay and Incentives/]
    T --> U[/Display Gross Salary/]
    U --> V[/Display Total Deductions/]
    V --> W[/Display Net Salary/]

    W --> X([STOP])


```
## 5. Python Source Code

```
# Employee Payroll and Deduction Analysis# Read employee detailsname = input("Enter Employee Name: ")emp_id = input("Enter Employee ID: ")# Read salary detailsbasic = float(input("Enter Basic Salary: "))allowances = float(input("Enter Allowances: "))overtime_hours = float(input("Enter Overtime Hours: "))overtime_rate = float(input("Enter Overtime Rate: "))incentives = float(input("Enter Incentives: "))# Calculate overtime payovertime_pay = overtime_hours * overtime_rate# Calculate gross salarygross_salary = basic + allowances + overtime_pay + incentives# Calculate progressive deductionsif gross_salary <= 20000:    deduction = gross_salary * 0.05elif gross_salary <= 40000:    deduction = 1000 + (gross_salary - 20000) * 0.10else:    deduction = 3000 + (gross_salary - 40000) * 0.15# Calculate net salarynet_salary = gross_salary - deduction# Display salary statementprint("\n====================================")print("          SALARY STATEMENT")print("====================================")print("Employee Name     :", name)print("Employee ID       :", emp_id)print("------------------------------------")print("Basic Salary      : Rs.", basic)print("Allowances        : Rs.", allowances)print("Overtime Pay      : Rs.", overtime_pay)print("Incentives        : Rs.", incentives)print("------------------------------------")print("Gross Salary      : Rs.", gross_salary)print("Total Deduction   : Rs.", deduction)print("------------------------------------")print("Net Salary        : Rs.", net_salary)print("====================================")
```

## 6. Sample Input

```
Enter Employee Name: Koteswara Rao
Enter Employee ID: EMP101
Enter Basic Salary: 25000
Enter Allowances: 5000
Enter Overtime Hours: 10
Enter Overtime Rate: 200
Enter Incentives: 3000
```

## 7. Sample Output

```
====================================
          SALARY STATEMENT
====================================
Employee Name     : Koteswara Rao
Employee ID       : EMP101
------------------------------------
Basic Salary      : Rs. 25000.0
Allowances        : Rs. 5000.0
Overtime Pay      : Rs. 2000.0
Incentives        : Rs. 3000.0
------------------------------------
Gross Salary      : Rs. 35000.0
Total Deduction   : Rs. 2500.0
------------------------------------
Net Salary        : Rs. 32500.0
====================================
```

## 8. Mermaid Flowchart Code

Use this code in your GitHub README or Mermaid Live Editor.

Invalid or unsupported diagram

## 9. Expected Result

The Python program successfully calculates the employee's gross salary, applies progressive deductions, and generates a formatted salary statement containing the employee details, total earnings, deductions, and final net salary.

Important: The deduction slabs above are assumed rules for this programming exercise, not actual statutory Indian payroll or income-tax rates.
