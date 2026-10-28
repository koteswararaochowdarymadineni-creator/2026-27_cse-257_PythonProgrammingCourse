
# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

eligible = []
ineligible = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Student name: ")
    aggregate = float(input("Aggregate percentage: "))

    count = int(input("Number of subjects: "))
    subjects = []

    for j in range(count):
        mark = float(input(f"Subject {j + 1} marks: "))
        subjects.append(mark)

    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income (Rs.): "))

    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if any(mark < MIN_SUBJECT_MARK for mark in subjects):
        reasons.append("Subject marks below 60")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income > MAX_INCOME:
        reasons.append("Family income above Rs. 250000")

    student = {
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income
    }

    if not reasons:
        eligible.append(student)
    else:
        ineligible.append((name, reasons))
      
eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].casefold()
    )
)

print("\n--- SCHOLARSHIP RANKING LIST ---")

if eligible:
    for rank, student in enumerate(eligible, start=1):
        print(
            f"Rank {rank}: {student['name']} | "
            f"Aggregate: {student['aggregate']}% | "
            f"Attendance: {student['attendance']}% | "
            f"Income: Rs. {student['income']:.0f}"
        )
else:
    print("No eligible students.")

print("\n--- INELIGIBLE STUDENTS ---")

if ineligible:
    for name, reasons in ineligible:
        print(name + ": " + ", ".join(reasons))
else:
    print("No ineligible students.")

print("\nProgram completed.")

