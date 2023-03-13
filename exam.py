# Prompt the user to enter their first name, last name, and academic year
first_name = input('Please enter First Name:')
last_name = input('Please enter Last Name:')
academic_year = int(input('Please enter Academic Year:'))

# Calculate the name of the student by concatenating the first and last name
name_of_student = first_name + " " + last_name

# Prompt the user to enter their marks for test 1 and test 2
test1 = int(input('Please enter Marks for test one:'))
test2 = int(input('Please enter Marks for test two:'))

# Determine the best test score and calculate the average of the test and coursework marks
if test1 >= test2:
    test_mark = test1
else:
    test_mark = test2

cswork = int(input('Please enter coursework Marks:'))
avg_test_cswork = (cswork + test_mark) / 2

# Calculate the final test and coursework marks and the final exam marks
final_test_cswork = avg_test_cswork * 0.4
end_of_semester_exam_marks = int(input('Please enter semester exam marks:'))
final_exam_mark = end_of_semester_exam_marks * 0.6

# Calculate the total marks and the result message based on the pass mark of 50
total_marks = final_test_cswork + final_exam_mark

if total_marks > 100:
    message = 'Error: Total marks should be between 0 and 100'
elif total_marks >= 50:
    message = 'Pass'
else:
    message = 'Fail'

# Prompt the user to enter the course unit and course code
course_unit = input('Please enter course unit: ')
course_code = input('Please enter course code: ')

# Write the student's details and marks to a text file
# with open('marks.txt', 'w') as f:
#     f.write(f"Student Name: {name_of_student}\n")
#     f.write(f"Academic Year: {academic_year}\n")
#     f.write(f"Course Unit: {course_unit}\n")
#     f.write(f"Course Code: {course_code}\n")
#     f.write(f"Final Test and Coursework Marks: {final_test_cswork}\n")
#     f.write(f"Final Exam Marks: {final_exam_mark}\n")
#     f.write(f"Total Marks: {total_marks}\n")
#     f.write(f"Result: {message}\n")
with open('marks.txt', 'w') as f:
    f.write("Student Name: " + name_of_student + "\n")
    f.write("Academic Year: " + str(academic_year) + "\n")
    f.write("Course Unit: " + course_unit + "\n")
    f.write("Course Code: " + course_code + "\n")
    f.write("Final Test and Coursework Marks: " + str(final_test_cswork) + "\n")
    f.write("Final Exam Marks: " + str(final_exam_mark) + "\n")
    f.write("Total Marks: " + str(total_marks) + "\n")
    f.write("Result: " + message + "\n")


# Print a message indicating that the marks have been saved to the file
print("Marks saved in 'marks.txt' file")
