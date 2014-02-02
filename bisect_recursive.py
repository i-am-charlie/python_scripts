"""
Filename: bisec_recursive.py
Author: i.am.charlie
LastModified: 02/01/2014

"""


def bisect(f, a, b, tol=10e-5):
	"""
	Implements the bisection root finding algorithm, assuming that f is a 
	real-valued function on [a, b] satisfying f(a) < 0 < f(b).
	"""
	lower, upper = a, b

	middle = 0.5 * (upper + lower)

	if upper-lower < tol:
		return middle

	else:
		print('Current mid point = {}'.format(middle))
		if f(middle) > 0:
			bisect(f, lower, middle)
		else:
			bisect(f, middle, upper)
