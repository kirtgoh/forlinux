#!/usr/bin/python3

def main():
	for n in inclusive_range():
		print(n, end=' ')	

def inclusive_range(*args):
	numargs = len(args)
	if numargs < 1: 
		raise TypeError('requires at least 1 argument')
	elif numargs == 1:
		(start, step) = (0, 1)
		stop = args[0]
	elif numargs == 2:
		(start, stop) = args
		step = 1
	elif numargs == 3:
		(start, stop, step) = args
	else:
		raise TypeError('inclusive_range at most need 3 arguments, get {}'.format(numargs))

	i = start
	while i <= stop:
		yield i
		i += step 

if __name__ == '__main__':
	main()
