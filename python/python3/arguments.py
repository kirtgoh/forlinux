#!/usr/bin/python3

def main():
	testfunc(5,6,7, 42,43,44, one=1, two=2,three=3)

def testfunc(this, that, other, *args, **kwargs):
	print("this is test func", this, that, other, args)
	for k in kwargs:
		print(k, kwargs[k])	

if __name__ == '__main__':
	main()
