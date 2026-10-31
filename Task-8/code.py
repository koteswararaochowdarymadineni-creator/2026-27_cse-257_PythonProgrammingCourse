# Multi-Currency Travel Budget Analysis

print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

# Input base currency and budget
base_currency = input("Enter base currency: ").upper()
budget = float(input("Enter travel budget: "))

n = int(input("Enter number of expense categories: "))

total_expense = 0
largest_expense = 0
largest_category = ""

# Process multiple expenses
for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")

    amount = float(input("Enter expense amount: "))

    currency = input("Enter currency code: ").upper()

    exchange_rate = float(input("Enter exchange rate: "))

    fee_percent = float(input("Enter conversion fee percentage: "))

    # Convert expense into base currency
    converted_amount = amount * exchange_rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_percent / 100

    # Calculate final expense
    final_expense = converted_amount + conversion_fee

    # Add to total expense
    total_expense += final_expense

    # Find largest expense category
    if final_expense > largest_expense:
        largest_expense = final_expense
        largest_category = category

    # Display individual expense
    print("Converted Amount:", round(converted_amount, 2))
    print("Conversion Fee:", round(conversion_fee, 2))
    print("Final Expense:", round(final_expense, 2))


# Compare expenditure with budget
print("\n------ TRAVEL BUDGET SUMMARY ------")

print("Base Currency:", base_currency)
print("Total Budget:", round(budget, 2))
print("Total Expenditure:", round(total_expense, 2))

if total_expense > budget:
    exceeded = total_expense - budget
    print("Budget Status: Budget Exceeded")
    print("Exceeded Amount:", round(exceeded, 2))

else:
    remaining = budget - total_expense
    print("Budget Status: Within Budget")
    print("Remaining Budget:", round(remaining, 2))

# Display largest expense
print("Largest Expense Category:", largest_category)
print("Largest Expense Amount:", round(largest_expense, 2))

print("-----------------------------------")
print("Analysis Completed")
