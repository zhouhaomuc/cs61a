""" implement luhn algorithm
	call luhn_sum and luhn_sum_double recursively
	when n < 10 is reached, stop the recursion
"""
def luhn_sum(n):
	if n < 10:
		return n
	else:
		remain, last = n // 10, n % 10
		return luhn_sum_double(remain) + last

def luhn_sum_double(n):
	if n < 10:
		return n*2
	else:
		remain, last = n // 10, n % 10
		return luhn_sum(remain) + 2 * last