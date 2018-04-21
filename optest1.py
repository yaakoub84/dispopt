import numpy as np
from scipy.optimize import minimize
a=np.array([0.0015 , 0.0018 , 0.0013 , 0.0051 ,0.0047, 0.049, 0.07 ])
b=np.array([1.42 , 2.28 , 2.23 , 1.23 , 1.10 , 1.62 , 1.15])
c=np.array([16.07 , 3.32 , 5.26 , 9.25 , 13.785 , 7.86 , 11.022 ])
pmin=[260,70,70,220,220,40,40]
pmax=[360,120,120,420,420,120,120]
bnds=((pmin[0],pmax[0]),(pmin[1],pmax[1]),(pmin[2],pmax[2]),(pmin[3],pmax[3]),(pmin[4],pmax[4]),(pmin[5],pmax[5]),(pmin[6],pmax[6]))
print (bnds)   
def objective(x):
    f=sum(c)
    for i in range(len(a)):
        f=f+a[i]*x[i]*x[i] + b[i]*x[i]
    return f
def constraint1(x):
    sum_eq = 1600
    con=sum(x)-sum_eq
    return con
con2 = {'type': 'eq', 'fun': constraint1}
cons = con2
n=len(b)
x0=np.zeros(n)
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)
print(solution)
