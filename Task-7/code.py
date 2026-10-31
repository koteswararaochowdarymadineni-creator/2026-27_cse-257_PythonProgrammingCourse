# Manufacturing Cost and Profitability Analysis

# Input section
quantity = int(input("Enter number of products: "))

material_cost = float(input("Enter material cost per unit: "))

labour_cost = float(input("Enter labour charges per unit: "))

wastage_percent = float(input("Enter wastage percentage: "))

machine_cost = float(input("Enter total machine cost: "))

selling_price = float(input("Enter selling price per unit: "))

profit_target = float(input("Enter profit target percentage: "))


# Process section
total_material = quantity * material_cost

total_labour = quantity * labour_cost

wastage_cost = (total_material * wastage_percent) / 100

total_manufacturing_cost = (
    total_material +
    total_labour +
    wastage_cost +
    machine_cost
)

total_revenue = quantity * selling_price

profit = total_revenue - total_manufacturing_cost

cost_per_unit = total_manufacturing_cost / quantity

profit_percentage = (
    profit / total_manufacturing_cost
) * 100


# Output section
print("\n----- MANUFACTURING COST REPORT -----")

print("Total Products:", quantity)

print("Total Material Cost:", total_material)

print("Total Labour Cost:", total_labour)

print("Wastage Cost:", wastage_cost)

print("Machine Cost:", machine_cost)

print("Total Manufacturing Cost:", total_manufacturing_cost)

print("Cost Per Unit:", cost_per_unit)

print("Total Selling Revenue:", total_revenue)

print("Profit / Loss:", profit)

print("Profit Percentage:", profit_percentage, "%")


# Profit target analysis
print("\n----- PROFITABILITY ANALYSIS -----")

if profit < 0:
    print("Production Result: LOSS")

elif profit_percentage >= profit_target:
    print("Production Result: PROFIT TARGET ACHIEVED")

else:
    print("Production Result: PROFIT TARGET NOT ACHIEVED")
