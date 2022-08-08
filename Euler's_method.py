

#Euler's method of solution of differential equation(1st order Runge kutta)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# (dy/dx) = (x+y), initial value: y=1.0 when x=0.0
# find y when x=0.05 and x=0.1, h=0.05

def f(x,y):
    return (x+y)
ff=open('Result.txt','w')
xs,h=np.linspace(0.0,1.0,20,retstep=True)
xi=xs[0]
xf=xs[-1]
x=xi
ys=1.0 # initial condition for y i.e,y(0)
print('x    y')
while(x<=xf):
    print(x,ys)
    print(>>ff,x,ys)
    ys+=h*f(x,ys)
    x+=h
ff.close()
sol=odeint(f,0.05,xs) #function,initial input of x array
P=np.loadtxt('Result.txt')
plt.plot(xs,sol,'+',label="scipy.odeint plot",c='blue')
plt.plot(P[:,0],P[:,1],'o',c='r',label="algorithm plot")
plt.title("Euler forward method solution of differential equation")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

