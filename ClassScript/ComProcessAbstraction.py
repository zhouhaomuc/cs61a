import math
def identity(n):
	""" return the same number

	>>> identity(9)
	9
	"""
	return n

def cube(n):
	"""return the cube result of the n

	>>> cube(3)
	27
	"""
	return pow(n, 3)

def common(n, term):
	""" calculate the result with abstraction

	>>> common(3, cube)
	36
	"""
	k, total = 1, 0
	while k <= n:
		k, total = k + 1, total + term(k) 
	return total