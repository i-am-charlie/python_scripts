""" This is a small program that calculates the first 'x' fibonacci numbers.
	This was written to initialize a git repository of all of my exploratory
	python scripts.
	"""

def fibo(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	else:
		return fibo(x-2) + fibo(x-1)
