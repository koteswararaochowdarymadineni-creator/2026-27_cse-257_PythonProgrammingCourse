

# Problem: Find the most economical eligible mobile plan

usage_data = float(input("Enter required data usage (GB): "))
usage_calls = int(input("Enter required call minutes: "))
required_validity = int(input("Enter required validity days: "))
budget = float(input("Enter your budget (Rs): "))

n = int(input("Enter number of mobile plans: "))

plans = []
eligible_plans = []

for i in range(n):
    print("\nEnter details of Plan", i + 1)

    name = input("Enter plan name: ")
    price = float(input("Enter base price: "))
    data = float(input("Enter included data (GB): "))
    calls = int(input("Enter included call minutes: "))
    validity = int(input("Enter validity days: "))
    extra_data_rate = float(input("Extra data charge per GB: "))
    extra_call_rate = float(input("Extra call charge per minute: "))

    # Calculate excess usage
    extra_data = max(0, usage_data - data)
    extra_calls = max(0, usage_calls - calls)

    # Calculate additional charges
    data_charge = extra_data * extra_data_rate
    call_charge = extra_calls * extra_call_rate

    # Calculate total cost
    total_cost = price + data_charge + call_charge

    plans.append((name, total_cost, validity))

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Extra Data Charge: Rs.", data_charge)
    print("Extra Call Charge: Rs.", call_charge)
    print("Total Cost: Rs.", total_cost)

    # Check eligibility
    if validity >= required_validity and total_cost <= budget:
        eligible_plans.append((name, total_cost, validity))

# Display result
print("\n----- PLAN COMPARISON -----")

if len(eligible_plans) > 0:

    best_plan = min(eligible_plans, key=lambda x: x[1])

    print("Eligible Plans:")

    for plan in eligible_plans:
        print(plan[0], "- Rs.", plan[1])

    print("\n----- BEST PLAN -----")
    print("Plan Name:", best_plan[0])
    print("Total Cost: Rs.", best_plan[1])
    print("Validity:", best_plan[2], "days")
    print("Most Economical Eligible Plan Found!")

else:
    print("No eligible plan found within your budget.")

print("\nProgram Completed.")

