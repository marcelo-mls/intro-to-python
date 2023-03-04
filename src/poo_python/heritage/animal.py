# Super classe

class Animal:
    def __init__(self, name, legs, flies=False):
        self.name = name
        self.legs = legs
        self.flies = flies

    def noise(self):
        print(f"{self.name} made a noise")

    def fly(self):
        if self.flies:
            print(f"{self.name} can fly, because it has wings")
        else:
            print(f"{self.name} doesn't fly")
