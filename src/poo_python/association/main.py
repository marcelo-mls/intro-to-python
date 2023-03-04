# Associação uma Classe FAZ USO outra classe

from writer import Writer
from pen import Pen
from typewriter import Typewriter

the_writer = Writer("Marcelo")
other_writer = Writer("Mellissa")

the_pen = Pen("Red")
the_typewriter = Typewriter("Wood")

print(the_writer.name)
print(other_writer.name)
print(the_pen.color)
print(the_typewriter.type)

print(the_pen.write())
print(the_typewriter.write())

the_writer.work()
other_writer.work()

the_writer.tool = the_pen  # Association
other_writer.tool = the_typewriter  # Association

print(the_writer.tool.write())
print(other_writer.tool.write())

the_writer.work()
other_writer.work()
