import numpy as np
import matplotlib.pyplot as plt

# JS Animation import is available at http://github.com/jakevdp/JSAnimation
from JSAnimation.IPython_display import display_animation
from matplotlib import animation

import ScaledConjugateGradient as SCG
reload(SCG)

def parabola(x,xmin,s):
    d = x - xmin
	return np.dot(np.dot(d,S),d.T)

def parabolaGrad(x,xmin,s):
	d = x - xmin
	return 2 * np.dot(d,s)

# rename as f and df (like previous example)
f = parabola
df = parabolaGrad
center = np.array([5,5])
S = np.array([[5,4],[4,5]])

n = 10
xs = np.linspace(0,10,n)
ys = np.linspace(0,10,n)
X,Y = np.meshgrid(xs,ys)
both = np.vstack((X.flat,Y.flat)).T
nall = n*n
Z = np.zeros(nall)
for i in range(n*n):
    Z[i] = f(both[i,:],center,S)
Z.resize((n,n))

# Initialize the figure and draw f(x)
fig = plt.figure(figsize=(10,10))
ax = plt.gca()
ax.contourf(X,Y,Z,20,alpha=0.3)
ax.axis('tight')

x = np.random.uniform(0,10,2)

resultSCG = SCG.scg(x, f, df, center, S, xtracep=True, ftracep=True, xPrecision=0, fPrecision=0, nIterations=20)

resultSteepest = np.zeros((20,2))
for i in range(20):
    resultSteepest[i,:] = x
	x = x - 0.1 * df(x,center,S)


scglines = ax.plot(resultSCG['xtrace'][:,0], resultSCG['xtrace'][:,1],'go-')[0]
steepestlines = ax.plot(resultSteepest[:,0], resultSteepest[:,1],'ro-')[0]
ax.legend(('SCG','Steepest'))

def update(ignore):
    global x
	x = np.random.uniform(0,10,2)
	resultSCG = SCG.scg(x, f, df, center, S, xtracep=True, ftracep=True, xPrecision=0, fPrecision=0, nIterations=20)
	
	for i in range(20):
		resultSteepest[i,:] = x
		x = x - 0.08 * df(x,center,S) 
	
	scglines.set_data(resultSCG['xtrace'][:,0], resultSCG['xtrace'][:,1])
	steepestlines.set_data(resultSteepest[:,0], resultSteepest[:,1])
	
	return (scglines,steepestlines)



anim = animation.FuncAnimation(fig, update, 50)
display_animation(anim, default_mode='once')
