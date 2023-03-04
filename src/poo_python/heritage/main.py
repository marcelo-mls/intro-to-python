# Uma classe É outra classe
# Uma classe herda métodos e atributos de outra

from bird import Bird
from feline import Feline
from snake import Snake


chicken = Bird("Chicken", 2, flies=True)
chicken.fly()  # heritage

cat = Feline("Smilodon", 4, flies=True)
cat.noise()  # heritage
cat.run()  # not heritage

cobra = Snake("King Cobra", 0)
cobra.fly()  # heritage
cobra.crawl()  # not heritage
# cobra.run() - esse método é exclusivo de Feline
