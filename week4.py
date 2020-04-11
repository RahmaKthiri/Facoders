grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

grade = ""
student = ""
marks = ""
i = ""



def students_names(grade):
    grade = input("Enter the grade: ")
    if grade == "grade_one":
        print(list(grade_one.keys()))
        end(i)
    elif grade == "grade_two":
        print(list(grade_two.keys()))
        end(i)
    elif grade == "grade_three":
        print(list(grade_three.keys()))
        end(i)



def student_score(grade, student):
    grade = input("Enter the grade: ")
    student = input("Enter the student: ")

    if grade == 'grade_one' and student == 'Sami':
        marks = grade_one.get("Sami")
        print(sum(marks))
        end(i)

    elif grade == 'grade_one' and student == 'Ahmad':
        marks = grade_one.get('Ahmad')
        print(sum(marks))
        end(i)

    elif grade == 'grade_one' and student == 'Faris':
        marks = grade_one.get('Faris')
        print(sum(marks))
        end(i)

    elif grade == 'grade_one' and student == 'Salem':
        marks = grade_one.get('Salem')
        print(sum(marks))
        end(i)

    elif grade == 'grade_one' and student == 'Mahmoud':
        marks = grade_one.get('Mahmoud')
        print(sum(marks))
        end(i)

    elif grade == 'grade_two' and student == 'Lana':
        marks = grade_two.get('Lana')
        print(sum(marks))
        end(i)

    elif grade == 'grade_two' and student == 'Dina':
        marks = grade_two.get('Dina')
        print(sum(marks))
        end(i)

    elif grade == "grade_two" and student == 'Maha':
        marks = grade_two.get('Maha')
        print(sum(marks))
        end(i)

    elif grade == 'grade_two' and student == 'Abeer':
        marks = grade_two.get('Abeer')
        print(sum(marks))
        end(i)

    elif grade == 'grade_three' and student == 'Rima':
        marks = grade_three.get('Rima')
        print(sum(marks))
        end(i)

    elif grade == 'grade_three' and student == 'Tala':
        marks = grade_three.get('Tala')
        print(sum(marks))
        end(i)

    elif grade == 'grade_three' and student == 'Lamar':
        marks = grade_three.get('Lamar')
        print(sum(marks))
        end(i)

    elif grade == 'grade_three' and student == 'Rola':
        marks = grade_three.get('Rola')
        print(sum(marks))
        end(i)

    elif grade == 'grade_three' and student == 'Naya':
        marks = grade_three.get('Naya')
        print(sum(marks))
        end(i)

    elif grade == 'grade_three' and student == 'Rima':
        marks = grade_three.get('Rima')
        print(sum(marks))
        end(i)

    elif grade == "grade_three" and student == 'Dalal':
        marks = grade_three.get('Dalal')
        print(sum(marks))
        end(i)

    elif grade == 'grade_three' and student == 'Ola':
        marks = grade_three.get('Ola')
        print(sum(marks))
        end(i)



def students_count(grade):
    grade = input("Enter the grade: ")

    if grade == "grade_one":
        print(len(grade_one))
        end(i)
    elif grade == "grade_two":
        print(len(grade_two))
        end(i)
    elif grade == "grade_three":
        print(len(grade_three))
        end(i)



def end(i):
    i = input("Enter done if you have finished OR more to continue: ")
    if i == "more":
        inputTeacher = input("Choose one: students_names, student_score, students_count: ")
        if inputTeacher == "students_names":
            students_names(grade)
        elif inputTeacher == "student_score":
            student_score(grade,student)
        elif inputTeacher == "students_count":
            students_count(grade)
    elif i == "done":
            quit()









inputTeacher = input("Choose one: students_names, student_score, students_count: ")
if inputTeacher == "students_names":
    students_names(grade)
elif inputTeacher == "student_score":
    student_score(grade,student)
elif inputTeacher == "students_count":
    students_count(grade)
