#!/usr/bin/python3

fh = open('../newfile.txt')
for line in fh.readlines():
	print(line, end='')

