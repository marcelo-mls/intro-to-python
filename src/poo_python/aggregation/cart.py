class Cart:
    def __init__(self):
        self.products = []

    def post_product(self, product):
        self.products.append(product)

    def get_products(self):
        for product in self.products:
            print(product.name, f'R$ {product.value:.2f}')

    def sum(self, formatted=False):
        total = 0
        for product in self.products:
            total += product.value
        if formatted:
            return f'R$ {total}'
        return total
