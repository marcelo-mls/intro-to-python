class Typewriter:
    def __init__(self, type):
        self.__type = type

    @property
    def type(self):
        return self.__type

    def write(self):
        return (f"using a typewriter made of {self.__type.lower()}.")
