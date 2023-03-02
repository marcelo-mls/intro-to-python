from datetime import datetime
from random import randint


class Person:
    greet = "Class Person initiate"
    current_year = int(datetime.strftime(datetime.now(), "%Y"))

    # 'Self' se refere a instancia que será criada
    def __init__(self, name, age, is_walking=False, is_speaking=False):
        self.name = name
        self.age = age
        self.is_walking = is_walking
        self.is_speaking = is_speaking

    print(greet)

    def walk(self):
        self.is_walking = True
        print(f"{self.name} started to walk.")

    def stop_walk(self):
        self.is_walking = False
        print(f"{self.name} stopped walk.")

    def speak(self, phrase):
        if self.is_speaking:
            print(f"{self.name} is already talking")
            return

        self.is_speaking = True
        print(f"{self.name} is saying: '{phrase}'")

    def stop_speak(self):
        self.is_speaking = False
        print(f"{self.name} stopped talking")

    # Método de instancia
    # Métodos que são relacionados a objeto que será instanciado
    # Recebe o 'self' (a instancia que será criada) como 1º argumento
    def get_birth_year(self):
        return self.current_year - self.age

    # Método de classe
    # Métodos que são relacionados a classe. independente da instancia
    # Recebe o 'cls' (ou qualquer nome, exemplo: this_class) como 1º argumento
    @classmethod
    def by_birth_date(this_class, name, birth_date):
        age = this_class.current_year - birth_date
        return this_class(name, age)

    # Método estático
    # Métodos que não depende nem da instancia nem da instancia
    # Não tem acesso ao 'self' ou 'cls'
    @staticmethod
    def set_id():
        id = randint(10000, 19999)
        return id

    # Getter
    @property
    def age(self):
        return self._age

    # Setter
    @age.setter
    def age(self, years_old):
        if isinstance(years_old, str):
            years_old = int(years_old)
        self._age = years_old

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, nomination):
        self._name = nomination.strip().title()
