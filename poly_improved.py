""" Earlier, we wrote a class with a couple attributes that evaluated and 
	differentiated the following polynomial expression:
		p(x) = a_0 + a_1*x + ... + a_N*x^N.

	This class definition is found in the file poly.py in this same repo.

	However, we build the following with efficiency in mind, building a
		function that evaluates the same expression, but uses NumPy arrays 
		along with array operations (namely, np.cumprod() ) for its computations,
		rather than any form of Python loop.

		(such functionality is already implemented as np.poly1d, but
		 for the sake of the exercise we don't use this class)
	"""
import numpy as np

def poly_eval(x, coeffs):
    y = np.empty(len(coeffs))
    y[1:] = x            # populates all elements of y vector with value 'x'
    y[0] = 1                    
    X=np.cumprod(y)         # creates a vector y = (1, x, x^2, ..., x^n)

    return np.dot(coeffs, X)    
