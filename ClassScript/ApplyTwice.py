"""High order function
a function that call another function twice"""
def apply_twice(f, n):
	return f(f(n))

def square(n):
	return n * n