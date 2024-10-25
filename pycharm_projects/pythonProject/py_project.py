print("Welcome to Mpangani Primary School!")

# Subject names
subjects = ["Mathematics", "English", "Kiswahili", "Science and Technology", "Social Studies", "CRE", "Home Science", "Art and Craft", "Agriculture", "Music"]

# Grade scale and points
grade_scale = {
    "A": (80, 100, 12),
    "A-": (75, 79, 11),
    "B+": (70, 74, 10),
    "B": (65, 69, 9),
    "B-": (60, 64, 8),
    "C+": (55, 59, 7),
    "C": (50, 54, 6),
    "C-": (45, 49, 5),
    "D+": (40, 44, 4),
    "D": (35, 39, 3),
    "D-": (30, 34, 2),
    "E": (0, 29, 1)
}

# Take input for student's name and class
student_name = input("Enter student's name: ")
class_name = input("What grade are you in?: ")

print("Welcome to", class_name, student_name, ".")

# Initialize a list to store marks
marks = []

# Loop through subjects to take input for marks
for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Calculate average grade
total_marks = sum(marks)
average_grade = total_marks / len(marks)

# Determine pass or fail and grade
for grade, (lower_bound, upper_bound, points) in grade_scale.items():
    if lower_bound <= average_grade <= upper_bound:
        print("Your average grade for term 3 is:", average_grade)
        print("Your grade for term 3 is:", grade)
        print("You earned", points, "points.")
        break
else:
    print("Your average grade for term 3 is:", average_grade)
    print("Sorry, we couldn't determine your grade.")

# Determine pass or fail
if average_grade >= 50:
    print("Congratulations! You passed.")
    print("You are promoted to the next class.")
else:
    print("Sorry, you failed.")
    print("You need to work harder to improve your grades.")
