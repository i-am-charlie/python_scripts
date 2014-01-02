class Polynomial:

	def __init__(self, coeffs):
		'''
		Creates an instance of the Polynomial class representing
			p(x) = a_0 x^0 + ... + a_N x^N,
		where a_i = coeffs[i].
		'''
		self.coeffs = coeffs

	def evaluate(self,x):
		"Evaluate the polynomial, returning p(x) for any x"
		pol = 0
		for a,b in enumerate(self.coeffs):
			pol += b * x ** a
		return pol

	def differentiate(self):
		'''
		Differentiate the polynomial, replacing the original coeffs
			with those of its derivative p'. 
			'''
		new_coeffs=[]
		for a,b in enumerate(self.coeffs):
			if a >= 1:
				new_coeffs.append(a*b)
		return new_coeffs
