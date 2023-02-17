import csv

with open("src/assets/unb_graduacao.csv", mode="r", encoding="utf-8") as file:
    content = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = content

group_by = dict()
for row in data:
    target = row[15]
    if target not in group_by:
        group_by[target] = 0
    group_by[target] += 1

with open("src/assets/unb_result.csv", mode="w", encoding="utf-8") as new_file:
    writer = csv.writer(new_file)

    headers = ["Target", "Contagem"]
    writer.writerow(headers)

    for target, count in group_by.items():
        row = [target, count]
        writer.writerow(row)

print("Operação realizada com sucesso !!!")
