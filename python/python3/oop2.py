#!/usr/bin/python3

# -- VIEW ---
class AnimalActions():
	def quack(self): return self._doAction('quack')
	def feather(self): return self._doAction('feather')
	def bark(self): return self._doAction('bark')
	def fur(self): return self._doAction('fur')

	def _doAction(self, action):
		if action in self.strings:
			return self.strings[action]
		else:
			return 'The {} has no {}'.format(self.animalName(), action)
	def animalName(self):
		return self.__class__.__name__.lower()

# --- MODEL ---
class Duck(AnimalActions):
	strings = dict(
			quack = 'Quaaaaak!',
			feather = 'The duck has white and grey feathers.',
	)

class Person(AnimalActions):
	strings = dict(
			quack = 'The person imitates a duck.',
			feather = 'The person takes a feather from the ground and shows it.',
			bark = 'The person says woof!',
			fur = 'The person puts on a fur coat.'
	)

class Dog(AnimalActions):
	strings = dict(
			bark = 'Arf!',
			fur = 'The dog has white fur with black spots.'
	)

def in_the_doghouse(dog):
	print(dog.bark())
	print(dog.fur())

def in_the_forest(duck):
	print(duck.quack())
	print(duck.feather())

def main():
	donald = Duck()	
	john = Person()
	fido = Dog()

	print("- In the doghouse:")
	for o in (donald, john, fido):
		in_the_doghouse(o)	

	print("- In the forest:")
	for o in (donald, john, fido):
		in_the_forest(o)

if __name__ == '__main__':
	main()			
