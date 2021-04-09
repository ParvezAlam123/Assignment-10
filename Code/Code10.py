import numpy as np
import matplotlib.pyplot as plt

x=np.sort(np.linspace(-2,2,100))
y=[]

for i in range(100):
    c=0
    for j in range(1000):
        a=np.random.choice(x)
        if x[i]==a:
            c=c+1
    y.append(c/1000)
    
f_x=[]
for i in range(100):
    sum=0
    for j in range(i+1):
        sum=sum+y[j]
    f_x.append(sum)
f_x=np.array(f_x)

g_x=[]
for i in range(100):
    a=x[i]/2
    sum=0
    for j in range(i+1):
        if x[j]<=a:
            sum=sum+y[j]
    g_x.append(sum)

g_x=np.array(g_x)
f_minus_g=f_x-g_x
t=[]

for i in range(100):
    t.append(f_minus_g[i]*x[i])
    
plt.scatter(x,f_x,marker='+',label='F(x)')
plt.scatter(x,g_x,marker='*',label='G(x)')
plt.scatter(x,t,label='[F(x)-G(x)]x')
plt.xlabel('x')
plt.legend()
plt.title('Simulation of [F(x)-G(x)]x')
plt.show()

    
    
   
    
    






    

        
        


        









