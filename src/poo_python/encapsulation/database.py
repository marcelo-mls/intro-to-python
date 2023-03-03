"""
public -> acessível dentro e fora da classe

protected -> acessível apenas na classe e subclasses (convenção: inicia _)

private -> acessível apenas dentro da própria classe (convenção: inicia __)
           acessível pela sintaxe (instancia._nomeDaClasse__nomeDoAtributo)

Na real, tudo é public mas, 'we are consenting adults'
"""


class Database:
    def __init__(self):
        self.__data = {}

    def post_client(self, id, name):
        if "clients" not in self.__data:
            self.__data["clients"] = {id: name}
        else:
            self.__data["clients"].update({id: name})

    def get_clients(self, id):
        for id, name in self.__data["clients"].items():
            print(id, name)

    def delete_client(self, id):
        del self.__data["clients"][id]

    # criar um getter para acessar o atributo privado
    @property
    def get_data(self):
        return self.__data
