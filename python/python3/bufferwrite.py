#!/usr/bin/python3

def main():
	fin = open('bigfile.txt', 'r')
	fout = open('newfile.txt', 'w')

	buffersize = 50000
	buffer = fin.read(buffersize)
	while len(buffer):
		fout.write(buffer)
		print('.', end=' ')
		buffer = fin.read(buffersize)

	print('Done.')

if __name__ == '__main__':
	main()

