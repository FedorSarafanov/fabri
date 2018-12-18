import numpy as np
from numpy import sqrt,pi
from matplotlib import pyplot as plt

def sin(x):
	return np.sin(x/180*np.pi)

def cos(x):
	return np.cos(x/180*np.pi)

def tan(x):
	return np.tan(x/180*np.pi)

def atan(x):
	return np.atan(x)/np.pi*180

wo=3
coeff=0.9
Shift=10
Z=8
H=wo*sqrt(1+(coeff*Z/wo**2)**2)
Rad=sqrt((Z+Shift)**2+H**2)

n=13
inside=0
scr=1
omegga=n/(Rad-Shift)/2*180/2

lena=1/(n/(Rad-Shift)/2)

if n%2==0:
	phhi=0
else:
	phhi=90
lefft=lena*inside/2

x=np.linspace(Shift-Rad,Rad-Shift,400)
print(Rad-Shift)
p=20.55
y=wo*sqrt(1+(coeff*x/wo**2)**2)*sin(omegga*x/(1/p*(np.abs(x)-p))+phhi)
plt.plot(x,y,x,-y)
plt.show()
# \addplot[name path=psinus1,sin,domain={-\Rad+\Shift:\Rad-\Shift},samples=400] {\wo*sqrt(1+(\coeff*x/\wo**2)**2)*sin(\omegga*x+\phhi)*(abs(x)<\lefft?\scr:1)} node[pos=.8, above]{};