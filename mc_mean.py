def f(x):
  return x**2+2*x+1
  
def mc(f,xmin,xmax,ymin,ymax,m,p):
  from numpy import random
  c=0
  for i in range(p):
    n=0
    x=random.rand(m)*(xmax-xmin)+xmin
    y=random.rand(m)*(ymax-ymin)+ymin
    for j in range(m):
      if f(x[j])>y[j] and y[j]>0: n+=1
      elif f(x[j])<y[j] and y[j]<0: n-=1
    c+=(ymax-ymin)*(xmax-xmin)*n/m
  return c/p

xmin=float(input('enter xmin:'))
xmax=float(input('enter xmax:'))
ymin=float(input('enter ymin:'))
ymax=float(input('enter ymax:'))
m=int(input('enter no. of points:'))
p=int(input('enter no.of cycles for mean value:'))
print('-'*30)
print(mc(f,xmin,xmax,ymin,ymax,m,p))
    