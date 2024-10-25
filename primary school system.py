# primary school system that will take marks, calculate average grade for term 3
# if grade is pass, print a form for next class else print fail and motivation statement and where to work hard.

print("Welcome to Mpangani Primary School!")

subjects = ["Mathematics", "English", "Kiswahili", "Science and Technology", "Social Studies", "CRE", "Home Science", "Art and Craft", "Agriculture", "Music"]

# Take students name and class
student_name = input("Enter student's name: ")
class_name = input("What grade are you in ?: ")

print("Welcome to", class_name, student_name, "." )

marks = []

# Loop through subjects to take input for marks
for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Calculate average grade
#total_marks = sum(marks)
#average_grade = total_marks / len(marks)

# Determine pass or fail
#if average_grade >= 50:
  #  print("Congratulations! You passed.")
 #   print("You are promoted to the next class.")
#else:
  #  print("Sorry, you failed.")
 #   print("You need to work harder to improve your grades.")

# Optionally, you can print the average grade
#print("Your average grade for term 3 is:", average_grade)
