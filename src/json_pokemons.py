import json

with open("src/assets/pokemons.json", "r") as file:  # with já fecha o arquivo
    pokemons_file = json.load(file)["results"]

pokemons_types = set()
for pokemon in pokemons_file:
    for type in pokemon["type"]:
        pokemons_types.add(type)

for type in pokemons_types:
    print("-->", type)
chosen_type = input("Digite um tipo de Pokemon... ").capitalize()

pokemons_of_type = [
    pokemon["name"]
    for pokemon in pokemons_file
    if chosen_type in pokemon["type"]
]

final_list = dict()
final_list[chosen_type] = pokemons_of_type

with open("src/assets/pokemons_type.json", "w") as type_file:
    json.dump(final_list, type_file)

print("Operação realizada com sucesso !!!")
