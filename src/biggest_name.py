def find_biggest_name(names: list[str]) -> str:
    """Recebe uma lista de nomes e retorna o de maior nº de caracteres."""
    biggest = names[0]

    for name in names:
        if len(name) > len(biggest):
            biggest = name

    return biggest


print(find_biggest_name(["Karl Marx", "Mao Tsé-Tung", "Che Guevara"]))
print(find_biggest_name(["React", "Vue", "Angular"]))
