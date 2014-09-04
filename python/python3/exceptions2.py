#!/usr/bin/python3

def main():
	try:
		for line in readfile('raven.doc'): print(line.strip())	
	except IOError as e:
		print("could not open file: ", e)
	except ValueError as e:
		print('bad filename', e)

def readfile(filename):
	if filename.endswith('.txt'):
		fh = open(filename)
		return fh.readlines()
	else: raise ValueError('Filename must end with .txt')

if __name__ == '__main__':
	main()
