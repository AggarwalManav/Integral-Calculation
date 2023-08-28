def f(x):
  return x**2+2*x+1
  
def mc(f,xmin,xmax,ymin,ymax,m):
  from numpy import random
  n=0
  x=random.rand(m)*(xmax-xmin)+xmin
  y=random.rand(m)*(ymax-ymin)+ymin
  for i in range(m):
    if f(x[i])>y[i] and y[i]>0: n+=1
    elif f(x[i])<y[i] and y[i]<0: n-=1
  return (ymax-ymin)*(xmax-xmin)*n/m

xmin=float(input('enter xmin:'))
xmax=float(input('enter xmax:'))
ymin=float(input('enter ymin:'))
ymax=float(input('enter ymax:'))
m=int(input('enter no. of points:'))
print('-'*30)
print(mc(f,xmin,xmax,ymin,ymax,m))
    
         



#try to rum mc method around 10 times and get error corresponding to mean value
#plot the error using matplotlib
#learn to plot error along 2 variables