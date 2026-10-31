import math

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transportation cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Validation
if (venue < 0 or equipment < 0 or transport < 0 or
    catering < 0 or certificate < 0 or
    sponsorship < 0 or participants <= 0):

    print("Invalid input! Enter valid positive values.")

else:
    # Fixed and variable costs
    fixed_cost = venue + equipment + transport

    variable_cost = catering + certificate

    # Total event expenses
    total_expenses = fixed_cost + (variable_cost * participants)

    # Sponsorship shortfall
    sponsorship_shortfall = max(0, total_expenses - sponsorship)

    # Remaining fixed cost after sponsorship
    remaining_fixed = max(0, fixed_cost - sponsorship)

    # Participant contribution per person
    contribution = variable_cost + (
        remaining_fixed / participants
    )

    # Total participant contribution
    total_contribution = contribution * participants

    # Break-even registration count
    if remaining_fixed == 0:
        break_even = 0
    elif contribution > variable_cost:
        break_even = math.ceil(
            remaining_fixed / (contribution - variable_cost)
        )
    else:
        break_even = -1

    # Total available funds
    total_funds = sponsorship + total_contribution

    # Financial status
    balance = total_funds - total_expenses

    # Output
    print("\n===== EVENT FINANCIAL REPORT =====")

    print("Fixed Cost:", fixed_cost)
    print("Variable Cost Per Participant:", variable_cost)
    print("Total Event Expenses:", total_expenses)

    print("Sponsorship Amount:", sponsorship)
    print("Sponsorship Shortfall:", sponsorship_shortfall)

    print("Participant Contribution:", contribution)
    print("Total Participant Contribution:", total_contribution)

    print("Minimum Break-Even Registrations:", break_even)

    print("Total Available Funds:", total_funds)
    print("Final Balance:", balance)

    if break_even == -1:
        print("Status: Break-even is not possible.")
    else:
        print("Status: Event budget is balanced.")
