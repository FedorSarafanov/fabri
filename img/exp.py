import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(0,2,1000)
# x=2.4
# y=1
# x=np.sqrt(-np.log(y)/2)
y=np.exp(-2*x**2)

for i in range(0, len(y)):
	print('%s\t%s'%(x[i],y[i]))
# print(y)
# plt.ylim([0,1000])
# plt.plot(x,y)
# plt.plot(ffc,uuc,'o-', markersize=2, color='red', linewidth=1.5)
# plt.show()

# 4.1) ОЭ -- R1=0, C вкл, R2=1 кОм вкл, Uвх=136 мВ, Uвых=980мВ
# 4.2) ОЭ-ОК, R1=0, С вклю, R2 =1 ком вкл, Uвх=136 мВ, Uвых=1720мВ