#!/usr/bin/python3

import re

def main():
	fh = open("raven.txt","r")
	# 1 - search
	# for line in fh.readlines():
	# 	if re.search('(Len|Neverm)ore', line):
	# 		print(line, end='')

    # 2 - search using match object
	# for line in fh.readlines():
	# 	match = re.search('(Len|Neverm)ore', line)
	# 	if match:
	# 		print(match.group())
    
	# 3.1 - replace using substitute
	# for line in fh.readlines():
	# 	print(re.sub('(Len|Neverm)ore', '###', line), end = '')

	# 3.2 - search and replace
	# for line in fh.readlines():
	# 	match = re.search('(Len|Neverm)ore', line)
	# 	if match:
	# 		print(line.replace(match.group(), '###'), end = '')

	# 4 using compile pattern object more efficient
	pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
	for line in fh:
		if re.search(pattern, line):
			print(pattern.sub('###', line), end='')

if __name__ == '__main__':
	main()
