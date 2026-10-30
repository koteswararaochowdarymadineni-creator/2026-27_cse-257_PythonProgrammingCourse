
# Progressive Electricity Billing System

months = int(input("Enter number of months: "))

previous_bill = None
bills = []

for i in range(months):
    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units: "))

    if units <= 100:
        energy_charge = units * 1.50

    elif units <= 200:
        energy_charge = (100 * 1.50) + (units - 100) * 2.50

    elif units <= 300:
        energy_charge = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00

    else:
        energy_charge = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00

    fixed_charge = 50
    surcharge = energy_charge * 0.05
    if units < 100:
        rebate = energy_charge * 0.10
    else:
        rebate = 0
      
    total_bill = energy_charge + fixed_charge + surcharge - rebate

    bills.append((month, units, total_bill))

    print("Energy Charge: Rs.", round(energy_charge, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total_bill, 2))

    if previous_bill is not None:
        increase = ((total_bill - previous_bill) / previous_bill) * 100

        if increase > 30:
            print("Warning: Unusual Increase Detected!")

        elif increase > 0:
            print("Bill Increased:", round(increase, 2), "%")

        else:
            print("Bill Decreased or Remained Same.")

    previous_bill = total_bill
print("\n----- MONTHLY BILL SUMMARY -----")

for month, units, bill in bills:
    print(month, "- Units:", units,
          "Total Bill: Rs.", round(bill, 2))

print("\nTotal Amount:", round(sum(b[2] for b in bills), 2))
print("Average Bill:", round(sum(b[2] for b in bills) / months, 2))

