# # Brook University Grading System
# # for each semester a given student will write tests for a given Course Unit

# def tests(test1, test2):
#     # two tests will be taken, however, the best done of these will be considered.
#     if test1 >= test2:
#         return test1
#     else:
#         return test2

# # create an interactive interface where a given student will enter a student name, academic year, and test results from test1 and test2, inform of Marks.

# first_name = input('Please enter First Name:')
# last_name = input('Please enter Last Name:')
# name_of_student = f"{first_name} {last_name}"
# print(f"Student Name: {name_of_student}")

# academic_year = int(input('Please enter Academic Year:'))
# print(f"Academic Year: {academic_year}")

# test1 = int(input('Please enter Marks for test one:'))
# test2 = int(input('Please enter Marks for test two:'))

# def coursework():
#     cswork = int(input('Please enter coursework Marks:'))
#     test_mark = tests(test1, test2)
#     # test_mark represents the best done of the two semester tests.
#     avg_test_cswork = (cswork + test_mark) / 2
#     # a contribution of 40% is expected from the finaltestscswork to the FINAL COURSE UNIT MARK.
#     final_test_cswork = avg_test_cswork * 0.4
#     return final_test_cswork

# final_test_cswork = coursework()
# print(f"Final Test and Coursework Marks: {final_test_cswork}")

# end_of_semester_exam_marks = int(input('Please enter semester exam marks:'))
# final_exam_mark = end_of_semester_exam_marks * 0.6
# # a contribution of 60% to the final COURSE UNIT MARK.
# print(f"Final Exam Marks: {final_exam_mark}")

# def final_course_unit_mark():
#     total_marks = final_test_cswork + final_exam_mark
#     # passmark = 50
#     if total_marks > 100:
#         message = 'Error: Total marks should be between 0 and 100'
#     elif total_marks >= 50:
#         message = 'Pass'
#     else:
#         message = 'Fail'
#     return (total_marks, message)

# total_marks, result_message = final_course_unit_mark()
# print(f"Total Marks: {total_marks}")
# print(f"Result: {result_message}")

# course_unit = input('Please enter course unit: ')
# course_code = input('Please enter course code: ')

# # writing the txt file make sure that the user gets a message of the location of the file you have saved the file marks
# with open('marks.txt', 'w') as f:
#     f.write(f"Student Name: {name_of_student}\n")
#     f.write(f"Academic Year: {academic_year}\n")
#     f.write(f"Course Unit: {course_unit}\n")
#     f.write(f"Course Code: {course_code}\n")
#     f.write(f"Final Test and Coursework Marks: {final_test_cswork}\n")
#     f.write(f"Final Exam Marks: {final_exam_mark}\n")
#     f.write(f"Total Marks: {total_marks}\n")
#     f.write(f"Result: {result_message}\n")

# print("Marks saved in 'marks.txt' file")



first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')
academic_year =input('Please enter your academic year:')

# name of student
name_of_student = first_name +"" + last_name 