"""some test of assert in the functions"""
from math import pi
def area(r, constant):
	assert r >= 0, 'r should be >= zero'
	return r * r * constant

def circle_area(r):
	return area(r, pi)