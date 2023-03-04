# Na composição uma classe PERTENCE a outra classe
# Neste exemplo, endereço pertence ao cliente

from client import Client


c1 = Client('Marcelo', 28)
c1.post_address('Senhora de Oliveira', 'MG')
c1.post_address('Belo Horizonte', 'MG')
c1.post_address('Belém', 'PA')


c2 = Client('Mellissa', 21)
c2.post_address('Belo Horizonte', 'MG')
c2.post_address('Inhapim', 'MG')

c1.get_addresses()
print()
c2.get_addresses()
