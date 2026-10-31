
# Railway Fare and Reservation Calculator

print("===== RAILWAY FARE CALCULATOR =====")

# Distance input
distance = float(input("Enter journey distance in KM: "))

# Number of passengers
n = int(input("Enter number of passengers: "))

# Travel class
print("\nSelect Travel Class")
print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")
print("4. AC First Class")

choice = int(input("Enter your choice: "))

if choice == 1:
    rate = 1.0
    reservation = 20
    class_name = "Sleeper"
elif choice == 2:
    rate = 2.0
    reservation = 40
    class_name = "AC 3 Tier"
elif choice == 3:
    rate = 3.0
    reservation = 50
    class_name = "AC 2 Tier"
elif choice == 4:
    rate = 4.0
    reservation = 60
    class_name = "AC First Class"
else:
    print("Invalid class selection")
    exit()

# Distance slab calculation
if distance <= 100:
    base_rate = 1
elif distance <= 300:
    base_rate = 1.5
elif distance <= 500:
    base_rate = 2
else:
    base_rate = 2.5

basic_fare = distance * base_rate * rate

total_fare = 0

# Passenger details
for i in range(1, n + 1):

    print("\nPassenger", i)

    age = int(input("Enter passenger age: "))

    if age < 5:
        fare = 0
    elif age <= 11:
        fare = basic_fare * 0.50
    elif age >= 60:
        fare = basic_fare * 0.60
    else:
        fare = basic_fare

    passenger_total = fare + reservation

    print("Basic Fare:", fare)
    print("Reservation Fee:", reservation)
    print("Passenger Total:", passenger_total)

    total_fare += passenger_total

print("\nTotal Ticket Fare:", total_fare)

# Cancellation
cancel = input("Do you want to cancel tickets? (yes/no): ")

if cancel.lower() == "yes":
    penalty = total_fare * 0.25
    refund = total_fare - penalty

    print("Cancellation Penalty:", penalty)
    print("Refund Amount:", refund)

else:
    print("Cancellation Penalty: 0")
    print("Final Payable Amount:", total_fare)

print("\n===== THANK YOU =====")

