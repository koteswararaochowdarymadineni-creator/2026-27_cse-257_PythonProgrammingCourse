## 1. Problem Statement

Develop a Python program to calculate household electricity bills using progressive consumption slabs. The program should calculate energy charges, fixed charges, surcharges, and rebates. It should compare electricity bills across multiple months and identify unusual increases in consumption or billing amounts.

## 2. Algorithm

1. Start the program.
2. Read the number of months.
3. For each month, enter the month name and electricity units consumed.
4. Calculate energy charges using progressive slabs:
   - 0–100 units: ₹2 per unit.
   - 101–200 units: ₹3 per unit.
   - 201–300 units: ₹5 per unit.
   - Above 300 units: ₹7 per unit.
5. Add fixed charges of ₹50.
6. Calculate a surcharge of 5% on energy charges.
7. Apply a 10% rebate on energy charges if consumption is below 100 units.
8. Calculate the final electricity bill.
9. Store and display monthly bills.
10. Compare consecutive monthly bills.
11. Identify unusual increases greater than 30%.
12. Display the results.
13. Stop.

## 3. IPO (Input, Process, Output)
```mermaid 

flowchart TD
    A([Start]) --> B[/Enter number of months/]
    B --> C[/Enter month and units/]
    C --> D{Units <= 100?}
    D -->|Yes| E[Energy = Units * 2]
    D -->|No| F{Units <= 200?}
    F -->|Yes| G[Calculate first two slabs]
    F -->|No| H{Units <= 300?}
    H -->|Yes| I[Calculate first three slabs]
    H -->|No| J[Calculate all four slabs]
    E --> K[Add fixed charges]
    G --> K
    I --> K
    J --> K
    K --> L[Calculate 5% surcharge]
    L --> M{Units < 100?}
    M -->|Yes| N[Apply 10% rebate]
    M -->|No| O[Rebate = 0]
    N --> P[Calculate final bill]
    O --> P
    P --> Q[Store monthly bill]
    Q --> R{More months?}
    R -->|Yes| C
    R -->|No| S[Compare monthly bills]
    S --> T{Increase > 30%?}
    T -->|Yes| U[Display unusual increase alert]
    T -->|No| V[Display normal increase]
    U --> W([End])
    V --> W

```mermaid
## 4. Flowchart

[Electricity Billing Flowchart -Identification and solving of simple real life or scientific or technical problems, and developing flow charts for the same. | by Sakthi | Medium](https://images.openai.com/static-rsc-4/eG0-aVlgyYpxpQ4D4GptNZtDU-g6ikIWSwI63XiBer9cv8Nn7fthudj5MwXXiLxOjK7-iLIh4sge4dNjxAoXP4adxWJl6GIQ-FbaMbRJJBYK0OK8DRfiD04MfUYOfEczB-mHuICAj4fmYgIx4leUEjQXgRKREE9UXGFCibk7a-w?purpose=inline)

[medium.com](https://medium.com/%40techinfocse/identification-and-solving-of-simple-real-life-or-scientific-or-technical-problems-and-developing-6087eabf495f?utm_source=chatgpt.com)

## 5. Python Source Code

```
        energy = (100 * 2) + (units - 100) * 3    elif units <= 300:        energy = (100 * 2) + (100 * 3) + (units - 200) * 5    else:        energy = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7    # Fixed charges    fixed = 50    # Surcharge    surcharge = energy * 0.05    # Rebate    if units < 100:        rebate = energy * 0.10    else:        rebate = 0    # Final bill    total = energy + fixed + surcharge - rebate    bills.append([month, units, total])    print("\n----- Electricity Bill -----")    print("Month:", month)    print("Units Consumed:", units)    print("Energy Charges: Rs.", round(energy, 2))    print("Fixed Charges: Rs.", fixed)    print("Surcharge: Rs.", round(surcharge, 2))    print("Rebate: Rs.", round(rebate, 2))    print("Total Bill: Rs.", round(total, 2))# Compare monthly billsprint("\n----- Monthly Bill Comparison -----")for i in range(1, n):    previous = bills[i - 1][2]    current = bills[i][2]    increase = current - previous    if increase > 0:        percentage = (increase / previous) * 100        print(bills[i][0], "Bill Increased:",              round(percentage, 2), "%")        if percentage > 30:            print("Alert: Unusual Increase Detected!")    else:        print(bills[i][0], "Bill did not increase.")print("\nBilling Process Completed.")
```

## 6. Sample Input

```
Enter number of months: 3

Enter month name: January
Enter electricity units: 80

Enter month name: February
Enter electricity units: 150

Enter month name: March
Enter electricity units: 300
```

## 7. Sample Output

```
----- Electricity Bill -----
Month: January
Units Consumed: 80.0
Energy Charges: Rs. 160.0
Fixed Charges: Rs. 50
Surcharge: Rs. 8.0
Rebate: Rs. 16.0
Total Bill: Rs. 202.0

----- Electricity Bill -----
Month: February
Units Consumed: 150.0
Energy Charges: Rs. 350.0
Fixed Charges: Rs. 50
Surcharge: Rs. 17.5
Rebate: Rs. 0
Total Bill: Rs. 417.5

----- Electricity Bill -----
Month: March
Units Consumed: 300.0
Energy Charges: Rs. 1000.0
Fixed Charges: Rs. 50
Surcharge: Rs. 50.0
Rebate: Rs. 0
Total Bill: Rs. 1100.0

----- Monthly Bill Comparison -----
February Bill Increased: 106.68 %
Alert: Unusual Increase Detected!
March Bill Increased: 163.47 %
Alert: Unusual Increase Detected!

Billing Process Completed.
```

## 8. Mermaid Flowchart Code
```mermaid

```mermaid

## 9. Expected Result

The Python program successfully calculates electricity bills using progressive slabs, fixed charges, surcharges, and rebates. It compares monthly bills and identifies unusual increases greater than 30%.

Bro, important: These slab rates and charges are assumed values for your Python academic project, not official electricity tariff rates. You can use this as your project demonstration.
