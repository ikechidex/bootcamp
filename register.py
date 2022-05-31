from students import student

name = input("\nEnter name for new student: ")
age = input("\nEnter age for new student: ")
gender = input("Enter student gender: ")

test_student = student(name, age, gender)
print(f"Welcome to TechApprentice Academy.\n--------------\n STUDENT BIO.\n-------------\n Student Name: {test_student.name}.\n Student Age: {test_student.age}.\n Student Gender: {test_student.gender}")

test_student.enter_score()

print(f"\nSubjects for {test_student.name} are:\n{test_student.subjects}")
scores_dict = test_student.subjects

header = f"""
=================================
welcome to TechApprentice Academy.
FINAL RESULT SHEET.
---------------------------------
Student Name:   {test_student.name}
Student Age:    {test_student.age}
Student Gender: {test_student.gender}
=================================
"""
print(header)
print('Subjects:')
average_score = 0

for x in scores_dict.keys():
    y = scores_dict[x]
    print(f'{x}: {y[-1]}')
    average_score += y[-1]

Final_average = average_score / len(scores_dict)

remarks = ''
if Final_average <= 40:
    remarks = 'Poor!, "Reapeat course!"'
elif Final_average > 40 and Final_average <= 50:
    remarks = 'Fair!, "Re-take Test!"'
elif Final_average > 50 and Final_average <= 60:
    remarks = 'Passed!'
elif Final_average > 60 and Final_average <= 75:
    remarks = 'Good!, "Passed!"'
elif Final_average > 75 and Final_average <= 89:
    remarks = 'V.Good!, "Passed!"'
else:
    remarks = 'Excellent! "Passed!"'

    footer = f"""
    ===================================
    Average: {Final_average}
    Comment: {remarks}
    ===================================
    """
    print(footer)

