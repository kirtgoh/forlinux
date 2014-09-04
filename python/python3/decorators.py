#!/usr/bin/python3

class Duck():

	def __init__(self, **kwargs):
		self.properties= kwargs

	def quack(self):
		print("Quack!")

	def walk(self):
		print("Walks like a duck.")

	def get_property(self, k):
		return self.properties.get(k, None)

	def set_property(self, k, v):
		self.properties[k] = v

	@property
	def color(self):
		return self.properties.get('color', None)

	@color.setter
	def color(self, c):
		self.properties['color'] = c
	
	@color.deleter
	def color(self):
		del properties['color']
		
def main():
	donald = Duck()
	donald.color = 'blue'
	print(donald.color)


if __name__ == '__main__':
	main()
