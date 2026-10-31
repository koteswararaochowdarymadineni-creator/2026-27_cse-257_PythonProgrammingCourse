# Employee Payroll and Deduction Analysis

## 1. Problem Statement

Write a Python program to calculate an employee's gross salary using basic pay, allowances, overtime pay, and incentives. Apply progressive deductions based on the gross salary and calculate the net salary. Finally, generate a formatted salary statement displaying employee details, earnings, deductions, and net salary.

## 2. Algorithm

1. Start the program.
2. Read employee name and employee ID.
3. Read basic salary.
4. Read allowances.
5. Read overtime hours and overtime rate.
6. Read incentives.
7. Calculate overtime pay.
8. Calculate gross salary.
9. Check gross salary:
   - If gross salary is less than or equal to ₹20,000, deduction is 5%.
   - If gross salary is less than or equal to ₹40,000, deduction is ₹1,000 plus 10% of the amount above ₹20,000.
   - Otherwise, deduction is ₹3,000 plus 15% of the amount above ₹40,000.
10. Calculate net salary.
11. Display the formatted salary statement.
12. Stop the program.

## 3. Input – Process – Output (IPO)

| Input          | Process                      | Output           |
| -------------- | ---------------------------- | ---------------- |
| Employee name  | Calculate overtime pay       | Employee details |
| Employee ID    | Calculate gross salary       | Overtime pay     |
| Basic salary   | Apply progressive deductions | Gross salary     |
| Allowances     | Calculate net salary         | Total deductions |
| Overtime hours | Generate salary statement    | Net salary       |
| Overtime rate  |                              |                  |
| Incentives     |                              |                  |

## 4. Flowchart
```mermaid

flowchart TD
    A([START]) --> B[/Enter Employee Name and Employee ID/]

    B --> C[/Enter Basic Salary/]
    C --> D[/Enter Allowances/]
    D --> E[/Enter Overtime Hours/]
    E --> F[/Enter Overtime Rate/]
    F --> G[/Enter Incentives/]

    G --> H[Calculate Overtime Pay]
    H --> I[Overtime Pay = Hours * Rate]

    I --> J[Calculate Gross Salary]
    J --> K[Gross = Basic + Allowances + Overtime Pay + Incentives]

    K --> L{Gross Salary <= 20000?}

    L -- YES --> M[Deduction = Gross * 5%]
    L -- NO --> N{Gross Salary <= 40000?}

    N -- YES --> O[Deduction = 1000 + (Gross - 20000) * 10%]
    N -- NO --> P[Deduction = 3000 + (Gross - 40000) * 15%]

    M --> Q[Calculate Net Salary]
    O --> Q
    P --> Q

    Q --> R[Net Salary = Gross Salary - Deduction]

    R --> S[Prepare Salary Statement]

    S --> T[/Display Employee Name and ID/]
    T --> U[/Display Basic Salary and Allowances/]
    U --> V[/Display Overtime Pay and Incentives/]
    V --> W[/Display Gross Salary/]
    W --> X[/Display Total Deductions/]
    X --> Y[/Display Net Salary/]

    Y --> Z([STOP])


```
## 5. Python Source Code

```
# Employee Payroll and Deduction Analysis# Read employee detailsname = input("Enter Employee Name: ")emp_id = input("Enter Employee ID: ")# Read salary detailsbasic = float(input("Enter Basic Salary: "))allowances = float(input("Enter Allowances: "))overtime_hours = float(input("Enter Overtime Hours: "))overtime_rate = float(input("Enter Overtime Rate: "))incentives = float(input("Enter Incentives: "))# Calculate overtime payovertime_pay = overtime_hours * overtime_rate# Calculate gross salarygross_salary = basic + allowances + overtime_pay + incentives# Calculate progressive deductionsif gross_salary <= 20000:    deduction = gross_salary * 0.05elif gross_salary <= 40000:    deduction = 1000 + (gross_salary - 20000) * 0.10else:    deduction = 3000 + (gross_salary - 40000) * 0.15# Calculate net salarynet_salary = gross_salary - deduction# Display salary statementprint("\n========================================")print("           SALARY STATEMENT")
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
========================================
           SALARY STATEMENT
========================================
Employee Name     : Koteswara Rao
Employee ID       : EMP101
----------------------------------------
Basic Salary      : Rs. 25000.0
Allowances        : Rs. 5000.0
Overtime Pay      : Rs. 2000.0
Incentives        : Rs. 3000.0
----------------------------------------
Gross Salary      : Rs. 35000.0
Total Deduction   : Rs. 2500.0
----------------------------------------
Net Salary        : Rs. 32500.0
========================================
```

## 8. Mermaid Flowchart Code (Broad – Complete)


## 9. Expected Result

The program successfully calculates gross salary, overtime pay, progressive deductions, and net salary. It also displays a formatted salary statement containing complete employee payroll details.






