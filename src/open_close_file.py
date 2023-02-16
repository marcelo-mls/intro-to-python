# escrita
file = open("arquivo.txt", mode="w")
lines = ["Primeiro\n", "contato\n", "com\n", "a\n", "linguagem\n", "Python\n"]
file.writelines(lines)
file.write("Outro método\n")
print("Mais um método", file=file)
file.close()  # sempre lembrar de fechar

# leitura
read_file_again = open("arquivo.txt", mode="r")
content = read_file_again.read()
print(content)
read_file_again.close()  # sempre lembrar de fechar

# ler e iterar
read_file = open("arquivo.txt", mode="r")
for line in read_file:
    print(line)
read_file.close()  # sempre lembrar de fechar
