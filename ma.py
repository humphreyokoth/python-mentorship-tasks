def tests(test1, test2):
    if test1 >= test2:
        return test1
    elif test1 <= test2:
        return test2
    else:
        return test2

print("------Course details-----")
course_unit = input("please enter the name of the course unit: ")
course_code = input("please enter the course code: ")
year = input("please enter the  student academic year: ")
name = input("Please enter the students name: ")
print("-------Test Marks-----")
test1 = int(input("please enter the mark"))


if not name.isalpha():
    print("Name must be a string")
elif not all(20 <= mark <= 100 for mark in [test1, test2, course_work_mark, exammark]):
    print("Marks should be between 20 and 100")
else:
    final_grade = course_work(course_work_mark)
    print(final_grade)
    with open('final_exam.txt', 'w') as file:
        file.write(final_grade)
    print("Your grades have been saved in a text file.")
