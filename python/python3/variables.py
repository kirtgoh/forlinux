#!/usr/bin/python3

def main():
	# r indicates this is a raw string
	n = 42
	# s = r"This is a \nstring!"
	# s = "This is a {} string!".format(n)
# 	s = '''\
# this is a string
# line after line
# of text and more
# text.
# '''
# 	print(s)
	# d = { 'one':1, 'two':2, 'three':3, 'four':4 }
	d = dict(
			one = 1, two = 2, three = 3, four = 4, five = 'five'
	)

	d['seven'] = 7
	for k in sorted(d.keys()):
		print(k, d[k])


if __name__ == '__main__':
	main()

