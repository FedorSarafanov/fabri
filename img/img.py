from numpy import sqrt,sum,abs,sin,cos,exp,pi,arctan
import numpy as np
from matplotlib import pyplot as plt

z=np.linspace(-1*pi,1*pi,1000)

coeff=0.01
wo=0.1
F=arctan(coeff*z/wo**2)

y=cos(10*z+F)
y0=cos(10*z)
w=wo*sqrt(1+(coeff*z/wo**2)**2)
plt.ylim(-2,2)

print(F)
# plt.plot(z,w)
# plt.plot(z,-w)
plt.plot(z,y,'b')
plt.plot(z,y0,'r')
plt.show()