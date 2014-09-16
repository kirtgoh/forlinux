#!/usr/bin/python
# mod1.py

import mod2

var1 = None

def func1A():
	global var1
	var1 = 'A'
	mod2.func2()

def func1B():
	global var1
	print var1

if __name__ == '__main__':
	func1A()
