#!/usr/bin/python

# Example file for working with classes

class myClass():
	def method1(self):
		print "myClass method1"

	def method2(self, anotherString):
		print "myClass method2: " + anotherString

class anotherClass(myClass):
	def method1(self):
		myClass.method1(self)
		print "anotherClass method1"

	def method2(self):
		print "anotherClass method2"

		
def main():
	c = myClass()
	c.method1()
	c.method2("this is another string")

	a = anotherClass();
	a.method1()
	a.method2()

if __name__ == '__main__':
	main()
		
