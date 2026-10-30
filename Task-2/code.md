# Progressive Electricity Billing System – Python Program

## 1. Problem Statement

Develop a Python program to calculate household electricity bills based on multiple consumption slabs. The program should calculate energy charges, fixed charges, surcharges, and rebates. It should also compare electricity bills across several months and identify unusual increases in monthly bills.

## 2. Algorithm

1. Start the program.
2. Read the number of months.
3. For each month, enter the month name and electricity units consumed.
4. Calculate electricity charges based on consumption slabs:
   - 0–100 units: ₹1.50 per unit
   - 101–200 units: ₹2.50 per unit
   - 201–300 units: ₹4.00 per unit
   - Above 300 units: ₹6.00 per unit
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge on energy charges.
7. Apply a 10% rebate if energy consumption is below 100 units.
8. Calculate the final electricity bill.
9. Compare monthly bills.
10. Identify unusual increases when the bill increases by more than 30% compared to the previous month.
11. Display the monthly bill details.
12. Stop the program.

## 3. Flowchart
```mermaid

flowchart TD
    A([Start]) --> B[/Enter number of months/]
    B --> C[/Enter month name and units/]
    C --> D{Units <= 100?}

    D -->|Yes| E[Calculate 1.50 per unit]
    D -->|No| F{Units <= 200?}

    F -->|Yes| G[Calculate slab charges]
    F -->|No| H{Units <= 300?}

    H -->|Yes| I[Calculate slab charges]
    H -->|No| J[Calculate above 300 slab charges]

    E --> K[Add fixed charges]
    G --> K
    I --> K
    J --> K

    K --> L[Calculate 5% surcharge]
    L --> M{Units below 100?}

    M -->|Yes| N[Apply 10% rebate]
    M -->|No| O[No rebate]

    N --> P[Calculate final bill]
    O --> P

    P --> Q{Previous bill exists?}
    Q -->|Yes| R{Increase above 30%?}
    R -->|Yes| S[Display unusual increase]
    R -->|No| T[Display normal bill]
    Q -->|No| T

    S --> U{More months?}
    T --> U

    U -->|Yes| C
    U -->|No| V[Display monthly summary]
    V --> W([Stop])

```mermaid
## 4. Python Source Code

```
    elif units <= 200:        energy_charge = (100 * 1.50) + (units - 100) * 2.50    elif units <= 300:        energy_charge = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00    else:        energy_charge = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00    # Fixed charges    fixed_charge = 50    # Surcharge    surcharge = energy_charge * 0.05    # Rebate    if units < 100:        rebate = energy_charge * 0.10    else:        rebate = 0    # Total bill    total_bill = energy_charge + fixed_charge + surcharge - rebate    bills.append((month, units, total_bill))    print("Energy Charge: Rs.", round(energy_charge, 2))    print("Fixed Charge: Rs.", fixed_charge)    print("Surcharge: Rs.", round(surcharge, 2))    print("Rebate: Rs.", round(rebate, 2))    print("Total Bill: Rs.", round(total_bill, 2))    # Compare bills    if previous_bill is not None:        increase = ((total_bill - previous_bill) / previous_bill) * 100        if increase > 30:            print("Warning: Unusual Increase Detected!")        elif increase > 0:            print("Bill Increased:", round(increase, 2), "%")        else:            print("Bill Decreased or Remained Same.")    previous_bill = total_bill# Final summaryprint("\n----- MONTHLY BILL SUMMARY -----")for month, units, bill in bills:    print(month, "- Units:", units,          "Total Bill: Rs.", round(bill, 2))print("\nTotal Amount:", round(sum(b[2] for b in bills), 2))print("Average Bill:", round(sum(b[2] for b in bills) / months, 2))
```

## 5. Sample Input

```
Enter number of months: 3

Month 1
Enter month name: January
Enter electricity units: 80

Month 2
Enter month name: February
Enter electricity units: 150

Month 3
Enter month name: March
Enter electricity units: 250
```

## 6. Sample Output

```
Month 1
Energy Charge: Rs. 120.0
Fixed Charge: Rs. 50
Surcharge: Rs. 6.0
Rebate: Rs. 12.0
Total Bill: Rs. 164.0

Month 2
Energy Charge: Rs. 275.0
Fixed Charge: Rs. 50
Surcharge: Rs. 13.75
Rebate: Rs. 0
Total Bill: Rs. 338.75
Warning: Unusual Increase Detected!

Month 3
Energy Charge: Rs. 550.0
Fixed Charge: Rs. 50
Surcharge: Rs. 27.5
Rebate: Rs. 0
Total Bill: Rs. 627.5
Warning: Unusual Increase Detected!

----- MONTHLY BILL SUMMARY -----

January - Units: 80 Total Bill: Rs. 164.0
February - Units: 150 Total Bill: Rs. 338.75
March - Units: 250 Total Bill: Rs. 627.5

Total Amount: 1130.25
Average Bill: 376.75
```

## 7. Mermaid Flowchart Code
Note: This is an educational example using assumed electricity rates, not an official electricity tariff.

Exam tip: Practice the slab calculation, `if-elif-else`, `for` loop, and percentage increase formula. These are the main Python concepts used in this program.
