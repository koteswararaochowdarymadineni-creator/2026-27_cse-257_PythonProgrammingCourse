
# Progressive Electricity Billing System

bills = []

n = int(input("Enter number of months: "))

for i in range(n):

    month = input("\nEnter month name: ")
    units = float(input("Enter electricity units: "))

    if units <= 100:
        energy = units * 2

    elif units <= 200:
        energy = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7
      
    fixed = 50

    surcharge = energy * 0.05
  
    if units < 100:
        rebate = energy * 0.10
    else:
        rebate = 0

    total = energy + fixed + surcharge - rebate

    bills.append([month, units, total])

    print("\n----- Electricity Bill -----")
    print("Month:", month)
    print("Units Consumed:", units)
    print("Energy Charges: Rs.", round(energy, 2))
    print("Fixed Charges: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))


print("\n----- Monthly Bill Comparison -----")

for i in range(1, n):
    previous = bills[i - 1][2]
    current = bills[i][2]

    increase = current - previous

    if increase > 0:
        percentage = (increase / previous) * 100

        print(bills[i][0], "Bill Increased:",
              round(percentage, 2), "%")

        if percentage > 30:
            print("Alert: Unusual Increase Detected!")

    else:
        print(bills[i][0], "Bill did not increase.")

print("\nBilling Process Completed.")


