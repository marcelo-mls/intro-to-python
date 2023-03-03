from Database import Database

db = Database()

db.post_client(1, "Marcelo")
db.post_client(2, "Marques")
db.post_client(3, "Lana")
db.post_client(4, "Souza")
db.post_client(4, "Mellissa")
print(db._Database__data)

db.delete_client(2)
print(db._Database__data)

db.get_clients(id)

print(f'{db.get_data  =  }')
