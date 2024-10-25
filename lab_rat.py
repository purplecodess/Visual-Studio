Student_adm = int(input("Enter student's admission number: "))

Password = int(input("Enter password: "))

if Password == Student_adm:
    print("Welcome, admission", Student_adm, ".")
else:
    print("Wrong Password, Try again!")

Student_age = int(input("Enter student's age: "))

Primary_age = 14
secondary_age = 18
college_age = 19

if Student_age <= 14:
    print("Welcome to Primary level, admission", Student_adm, ".")
elif Student_age >= 19:
    print("Welcome to College level, admission", Student_adm, ".")
else:
    print("Welcome to Secondary level, admission", Student_adm, ".")

marks = int(input("Student's marks: "))

if marks <= 25:
    print("Below average, admission", Student_adm, ".")
elif marks >= 75:
    print("Well done, admission", Student_adm, ".")
else:
    print("Good, admission", Student_adm, ".")
