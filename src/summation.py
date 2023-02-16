numbers = input("Digite vários números. (separados por espaço) ")
array_of_numbers = numbers.split(" ")
summation = 0

for number in array_of_numbers:
    if number.isdigit():
        summation += int(number)
    else:
        print(f"Erro: {number} não é um caractere válido")


print(f"A soma é: {summation}")
