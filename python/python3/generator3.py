#!/usr/bin/python3

class inclusive_range():
	def __init__(self, *args):
		numargs = len(args)
		if numargs < 1: 
			raise TypeError('requires at least 1 argument')
		elif numargs == 1:
			(self.start, self.step) = (0, 1)
			self.stop = args[0]
		elif numargs == 2:
			(self.start, self.stop) = args
			self.step = 1
		elif numargs == 3:
			(self.start, self.stop, self.step) = args
		else:
			raise TypeError('inclusive_range at most need 3 arguments, get {}'.format(numargs))

	def __iter__(self):
		i = self.start
		while i <= self.stop:
			yield i
			i += self.step 
		
def main():
	for n in inclusive_range(25): print(n, end=' ')	


if __name__ == '__main__':
	main()
