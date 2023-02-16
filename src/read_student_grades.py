try:
    file = open("src/student_grades.txt", mode="r")
    new_file = open("src/student_disapproved.txt", mode="w")

    content = file.read()
    array_of_student = content.split("\n")

    for line in array_of_student:
        student = line.split(" ")
        if int(student[1]) < 6:
            print(student[0], file=new_file)
            print(student[0])

except OSError:
    print("arquivo inexistente")
else:
    print("arquivo manipulado e fechado com sucesso")
finally:
    print(file.closed, new_file.closed)
    file.close()  # sempre lembrar de fechar
    new_file.close()  # sempre lembrar de fechar
    print(file.closed, new_file.closed)
