from person import Person

person_one = Person("Marcelo", 28)

print(person_one.name)
print(f"{person_one.is_walking = }")
person_one.walk()
print(f"{person_one.is_walking = }")
person_one.stop_walk()
print(f"{person_one.is_walking = }")
print(person_one.is_speaking)
person_one.speak("Hello, World!")
print(person_one.is_speaking)
person_one.speak("Another thing!")
person_one.stop_speak()
print(person_one.is_speaking)
print(person_one.get_birth_year())
print("=" * 20)


person_two = Person("Mellissa", 2001)

person_two.walk()
person_two.speak("class method")
print(person_two.get_birth_year())
print(person_two.age)
print(person_two.set_id())
print(Person.set_id())
print("=" * 20)


person_three = Person("  sOuZA ", "1952")

print(person_three.get_birth_year())
print(person_three.age)
print(person_three.name)
print("=" * 20)
