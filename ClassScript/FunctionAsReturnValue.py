"""Function which returns a function"""
def addMore(n):
	"""
	>>> addThree = addMore(3)
	>>> addThree(4)
	7
	"""
	def adder(k):
		return n + k
	return adder