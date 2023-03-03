class Pen:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    def write(self):
        return (f"writing with a {self.__color.lower()} pen.")
