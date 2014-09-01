#!/usr/bin/python3

def isprime(n):
	if n == 1: return False

	for x in range(2, n):
		if n % x == 0: return False

	else:return True

def primes(n=1):
	while(True):
		if isprime(n): yield n
		n = n + 1

for i in primes():
	if i > 1000: break
	print(i)

