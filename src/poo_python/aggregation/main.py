# Uma classe TEM outra classe como parte de si
# Uma classe precisa da outra para funcionar corretamente
# Elas podem existir separadas, mas para funcionar precisam ser agregadas

from cart import Cart
from product import Product

my_cart = Cart()
p_phone = Product("Smartphone", 1300.70)
p_shirt = Product("Shirt", 40.98)
p_glue = Product("Glue", 2.49)

my_cart.post_product(p_phone)  # aggregation
my_cart.post_product(p_shirt)  # aggregation
my_cart.post_product(Product("Shirt", 40.98))  # aggregation
my_cart.post_product(p_glue)  # aggregation

my_cart.get_products()
print(my_cart.sum())
print(my_cart.sum(formatted=True))
