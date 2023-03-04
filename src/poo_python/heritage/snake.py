# Subclasse

from animal import Animal


class Snake(Animal):  # heritage
    def crawl(self):
        print(f'{self.name} is crawling')
