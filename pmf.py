""" We create an algorithm that will generate draws from a discrete probability
	distribution, with a given probability mass function, q.

	One way to implement the algorithm, given 'q', is as follows:
	"""
import numpy as np
from random import uniform
	
def sample(q):
    a = 0.0
    U = uniform(0,1)
    for i in range(len(q)):
    	if a < U <= a + q[i]:
	    return i
	a = a + q[i]

""" It is easy to see that x takes values in range(len(q)) with probability q[i].
	
	Now, we would like to implement this with a slightly faster algorithm that
	takes advantage of the NumPy library, avoiding explicit loops.  We achieve 
	this with the following object:
	"""
class discreteRV:
	def __init__(self, q):
	    self.probabilities = q    # data for instance of class is vec of probabilities

	def draw(self, k):
	   P = np.array(self.probabilities)
	   Q = P.cumsum()
	   result=[]
	   i=1
	   while i <= k:
	       u = uniform(0,1)	
	       result.append(Q.searchsorted(u)-1)
	       i += 1
	   return result
