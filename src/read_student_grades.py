try:
    file = open("src/student_grades.txt", mode="r")
    content = file.read()
    array_of_student = content.split("\n")
    new_file = open("src/student_disapproved.txt", mode="w")

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
    file.close()  # sempre lembrar de fechar
    new_file.close()  # sempre lembrar de fechar
