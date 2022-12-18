import numpy as np
import matplotlib.pyplot as plt
import random
import math

m=1
a=1/500
w=200
T=10

N=int(100)
A=int(10000)

E=np.zeros(N)
X=np.zeros(A)

Xmed=np.zeros(N)
Emed=np.zeros(int(N/T))

random.seed()

for j in range (N):
    for i in range(A):

        r = np.random.random(1)
        phi= np.random.random(1)
        z0=math.cos(2*math.pi*phi)*(-2*math.log(r))**(0.5)
        z1=math.sin(2*math.pi*phi)*(-2*math.log(r))**(0.5)

        # if (i==A-1):
        #     X[A-1]=(X[A-2]+X[0])/(2+(a*w)**2)+1/(2*m/a+m*a*w**2)**(0.5)*z0
        X[i]=(X[(i - 1) % N] + X[(i + 1) % N]) / (2 + (a*w)**2) + 1/(2*m/a + m*a*w**2)**(0.5)*z0
        # if (i==0):
        #     X[0]=(X[A-1]+X[1])/(2+(a*w)**2)+1/(2*m/a+m*a*w**2)**(0.5)*z0
        
        E[j]=E[j]+m*(w**2)*((X[i])**2)*0.5
        Xmed[j]=Xmed[j]+X[i]


SumOfE = 0

i = T
C = 0

while(i < N):
    SumOfE = SumOfE + E[i]/A
    i += T//2
    C += 1
    
SumOfE /= C

plt.figure(figsize=(12, 7))
plt.plot((E/A), 'o-r', alpha=0.7, label="<E>", lw=2, mec='b', mew=2, ms=3)
plt.plot([SumOfE] * N)
print(SumOfE)
plt.grid(True)
plt.legend()

plt.figure(figsize=(12, 7))
plt.plot((Xmed/A), 'purple', alpha=0.7, label="<X>", lw=2, mec='b', mew=2, ms=3)
plt.legend()
plt.grid(True)

plt.show()