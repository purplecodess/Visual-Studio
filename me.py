Chemistry_pass_mark = "75"

Chemistry_exam_marks = input("What is your mark?")

if Chemistry_exam_marks < Chemistry_pass_mark:
    
    print("Failed")

elif Chemistry_exam_marks == Chemistry_pass_mark:

    print("Average")

elif Chemistry_exam_marks > Chemistry_pass_mark:

    print("Passed")