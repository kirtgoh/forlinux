#!/usr/bin/python3

class AnimalActions():
	def quack(self): return self.strings['quack']
	def feather(self): return self.strings['feather']
	def bark(self): return self.strings['bark']
	def fur(self): return self.strings['fur']

class Duck(AnimalActions):
	strings = dict(
			quack = 'Quaaaaak!',
			feather = 'The duck has white and grey feathers.',
			bark = 'The duck cannot bark.',
			fur = 'The duck has no fur.'
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
			quack = 'The dog cannot quack.',
			feather = 'The dog has no feathers',
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
