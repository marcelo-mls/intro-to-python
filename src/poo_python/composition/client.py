from address import Address


class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = []

    def post_address(self, city, state):
        self.address.append(Address(city, state))  # Composition

    def get_addresses(self):
        for address in self.address:
            print(self.name, address.city, address.state)
