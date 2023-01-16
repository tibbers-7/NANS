import numpy as np
import matplotlib.pyplot as plt
from nans_lib_2 import  rk4N, least_squares_regression

# h"(t) = 3+cos(4t/3)- f(t)
# h(t0) = 0, h'(t0) = 1

#######################################################
    # a) koja kolicina vode se nalazi u sudu u trenutku t=20s?
ddhT = lambda t, hT, dhT: 3+ np.cos(4*t/3)-hT

t0 = 5
tb = 20
step = (tb - t0)/1000

nhT0 = np.array([0,1])

vRK4, _ = rk4N(t0, tb, step, nhT0, ddhT)
r = 15

#Zapremina u t=20
vEnd = (r**2)*np.pi*vRK4[-1]
print("U trenutku t=",tb,", zapremina V=",round(vEnd,2))

#Crtanje funkcije a)
x=np.arange(t0,tb+step,step)
plt.plot(x,vRK4, 'green', label="Visina a)")

#################################
# b)
#trazim max V (t in range(10,20))
t0=10
vRK4, _ = rk4N(t0, tb, step, nhT0, ddhT)
x=np.arange(t0,tb+step,step)
plt.plot(x,vRK4,'red', label="Visina b)")

p=least_squares_regression(x,vRK4,14)
f=lambda x: np.polyval(p,x)

maxX=t0
maxF=f(maxX)
for i in x:
    if (f(i)>maxF):
        maxF=f(i)
        maxX=i
vMax=r**2*np.pi*maxF
print("Maksimalna kolicina vode: V=",round(vMax,2)," h=",round(maxF,2)," t=",round(maxX,2))
plt.scatter(maxX,maxF,c="red",label="Max visina b)")



plt.legend()
plt.show()