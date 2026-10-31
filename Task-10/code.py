
# Examination Result and Grace-Mark Validation

n = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

max_marks = []
pass_marks = []

for i in range(subjects):
    print("\nSubject", i + 1)
    maximum = int(input("Enter maximum marks: "))
    passing = int(input("Enter pass marks: "))

    max_marks.append(maximum)
    pass_marks.append(passing)

grace_limit = int(input("\nEnter maximum grace marks allowed: "))

for student in range(n):

    print("\n----- Student", student + 1, "-----")

    name = input("Enter student name: ")

    marks = []
    final_marks = []

    for i in range(subjects):

        mark = int(input("Enter marks in subject " + str(i + 1) + ": "))

        if mark < 0 or mark > max_marks[i]:
            print("Invalid marks entered!")
            exit()

        # Apply grace marks if eligible
        if mark < pass_marks[i]:
            required = pass_marks[i] - mark

            if required <= grace_limit:
                mark = min(mark + required, max_marks[i])
                print("Grace marks applied in subject", i + 1)

        marks.append(mark)
        final_marks.append(mark)

    total = sum(final_marks)
    maximum_total = sum(max_marks)
    percentage = (total / maximum_total) * 100

    print("\n----- FINAL RESULT -----")
    print("Student Name:", name)

    for i in range(subjects):
        print("Subject", i + 1, ":", final_marks[i],
              "/", max_marks[i])

    print("Total Marks:", total, "/", maximum_total)
    print("Percentage:", round(percentage, 2), "%")

    # Check final result
    if all(final_marks[i] >= pass_marks[i]
           for i in range(subjects)):

        print("Result: PASS")

        if percentage >= 75:
            print("Classification: Distinction")
        elif percentage >= 60:
            print("Classification: First Class")
        elif percentage >= 50:
            print("Classification: Second Class")
        else:
            print("Classification: Third Class")

    else:
        print("Result: FAIL")
        print("Classification: Not Classified")

print("\nExamination Result Processing Completed!")

