
# Hospital Billing and Patient Classification
name = input("Enter patient name: ")
category = input("Enter patient category (Senior/Regular/Other): ").strip().lower()

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
  
    total_bill = consultation + diagnostic + treatment

    if category == "senior":
        discount_rate = 0.10
    elif category == "regular":
        discount_rate = 0.05
    elif category == "other":
        discount_rate = 0.0
    else:
        discount_rate = -1

    if discount_rate == -1:
        print("Invalid patient category!")

    else:
        discount = total_bill * discount_rate
        final_bill = total_bill - discount
        if final_bill < 5000:
            classification = "Low Payment"
        elif final_bill <= 10000:
            classification = "Medium Payment"
        else:
            classification = "High Payment"

        print("\n----- HOSPITAL BILL -----")
        print("Patient Name:", name)
        print("Patient Category:", category.title())
        print("Consultation Charges: Rs.", consultation)
        print("Diagnostic Charges: Rs.", diagnostic)
        print("Treatment Charges: Rs.", treatment)
        print("Total Bill: Rs.", total_bill)
        print("Discount: Rs.", discount)
        print("Final Bill: Rs.", final_bill)
        print("Patient Classification:", classification)

