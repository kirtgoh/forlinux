#!/usr/bin/python

def main():
	# 1. write file
	# f = open("textfile.txt", "w+")
    #
	# for i in range(10):
	# 	f.write("This is line %d\r\n" % (i+1))
    #
	# f.close()
    #
	# 2. apend file
	# f = open("textfile.txt", "a+")
    #
	# for i in range(10):
	# 	f.write("This is line %d\r\n" % (i+1))
    #
	# f.close()
    #
	# 3. read file
	f = open("textfile.txt", "r")
	if f.mode == "r":
	# 	contents = f.read()
	# print contents
		fl = f.readlines()
		for l in fl:
			print l

	f.close()


if __name__ == '__main__':
	main()

