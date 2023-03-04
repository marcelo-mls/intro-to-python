# Subclasse

from animal import Animal


class Feline(Animal):  # heritage
    def run(self):
        print(f'{self.name} is running')
