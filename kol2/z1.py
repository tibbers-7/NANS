import numpy as np
import matplotlib.pyplot as plt
from nans_lib_2 import integrate_simpson,zeroBisection

f=lambda x: np.sqrt(1-(abs(x)-1)**2)+np.pi
g=lambda x: np.arccos(1-abs(x))
h=lambda x: x+2

a=-2
b=2

plt.plot([a,b], [0, 0], 'k') 

def caseA(f,g,a,b):
    x=np.arange(a,b,0.001)
    fX=f(x)
    gX=g(x)
    hX=h(x)
    plt.plot(x,fX,'r',label="f(x)")
    plt.plot(x,gX,'r',label="g(x)")
    plt.plot(x,hX,'k',label="h(x)")


    #presek g i h
    pom2=lambda x: g(x)-h(x)
    hg=zeroBisection(pom2,a,b)[0]

    #presek f i h
    pom3=lambda x: f(x)-h(x)
    hf=zeroBisection(pom3,a,b)[0]

    #integral
    fminusg=lambda x: f(x)-g(x)
    fminush=lambda x: f(x)-h(x)
    hminusg=lambda x: h(x)-g(x)
    hminusf=lambda x: h(x)-f(x)

    P1=integrate_simpson(fminusg,a,hg,100)+ integrate_simpson(fminush,hg,hf,100)
    P2=integrate_simpson(hminusg,hg,b,100)- integrate_simpson(hminusf,hf,b,100)
    print("Povrsine:",round(P1,4),round(P2,4))

    P3=integrate_simpson(fminusg,a,b,100)
    print("Cela P:",round(P3,4))
    return P1,P2

#Zapremina
def caseB(f,g,a,b):
    povrsine=caseA(f,g,a,b)
    y= abs(povrsine[0]-povrsine[1])
    plt.plot([a,b],[y,y],'b',label="y")

    fSq=lambda x:(f(x)-y)**2
    V=np.pi*(integrate_simpson(fSq,a,b,100))
    print("Zapremina:",round(V,4))


caseB(f,g,a,b)
plt.legend()
plt.show()