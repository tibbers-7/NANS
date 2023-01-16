import numpy as np
import matplotlib.pyplot as plt
from nans_lib_2 import ddf,f,finiteDifference,least_squares_regression,zeroFalsePosition

# a) prikaz kretanja cene BTC
x = np.array([1, 5])
fX = np.array([137, 437])
h=(x[1]-x[0])/100

left= lambda *args: -np.cos(args[0]-2) * ddf(args[1])+ f(4*args[0]/3)
right= lambda *args: np.log(5/4 * args[0])- np.sin(13)

xA= np.arange(x[0],x[1]+h,h)
fXA= finiteDifference(left,right,x[0],fX[0], x[1], fX[1],h)
plt.plot(xA, fXA, 'orange', label="Kretanje BTC")

# b) Promet BTC
D=4 #petak
p=least_squares_regression(xA,fXA,14)
pD=np.polyval(p,D)
V=np.cos(pD)/3 *pD**3 *np.sin(D+2)
print("Promet za petak: V=",round(V,2))

# c) BTC dostize 700$
xC=np.linspace(x[0],x[1],100)
f=lambda x: np.polyval(p,x)-700
z1,_=zeroFalsePosition(f, 3.5, 4, 0.00001, 100)
z2,_=zeroFalsePosition(f, 4, 5, 0.00001, 100)
pZ1=np.polyval(p,z1)
pZ2=np.polyval(p,z2)

plt.scatter([z1,z2],[pZ1,pZ2], label="cena=700$")
zR1=round(z1,2)
zR2=round(z2,2)
print("Vreme kad je cena dostigla 700$:",zR1,zR2)

plt.legend()
plt.show()