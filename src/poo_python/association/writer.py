class Writer:
    def __init__(self, name):
        self.__name = name  # Private
        self.__tool = None  # Private

    @property
    def name(self):
        return self.__name

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool):
        self.__tool = tool

    def work(self):
        if self.__tool is None:
            print(f"{self.__name} can't write without a 'tool'")
        else:
            print(f"{self.__name} is {self.__tool.write()}")
