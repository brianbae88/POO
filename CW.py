def isPrime(x):
	if x == 1 or x == 0 or x < 0:
		return False
	for i in range (2, x):
		print i 
		if x % i == 0:
			return False
		else:
			return True

print isPrime(9)


def nthPrime(n):
	counter = 0
	integer = 0
	while counter < n:
		integer += 1
		if isPrime(integer) == True:
			counter += 1
		print counter, integer
	return integer

print nthPrime(3)