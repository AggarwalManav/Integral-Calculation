def f(x):
  return x**2+2*x+1

def simpsons(a,b,n,f):
  x0=a
  h=(b-a)/n
  x=a+h
  c=f(a)+f(b)
  for i in range(1,n):
    if x<=b:
      if i%2==0:
        c+=(2*f(x))
      else:
        c+=(4*f(x))  
      x0=x
      x+=h
  return c*h/3

a=float(input('enter a:'))
b=float(input('enter b:'))
n=int(input('enter no. of steps:'))
  
print('integral = ',simpsons(a,b,n,f))

"""
sir's code:

def simpson(f, a, b, n):
  if n % 2:
    raise ValueError("n must be even (received n=%d)" % n)
  h = (b - a) / n
  s = f(a) + f(b)
  for i in range(1, n, 2):
    s += 4 * f(a + i * h)
  for i in range(2, n-1, 2):
    s += 2 * f(a + i * h)
  return s * h / 3
  
from numpy import *            #these are for input of list in x and y 
def simp(x,y):
  n=len(x)
  if(n!=len(y)):
    raise ValueError('Len of x(=%d) & y(=%d) should match' % (n,len(y)))
  elif(mod(n,2)=0):
    raise ValueError('Len of x & y (=%d) should be an odd number' % n)
  h=abs(x[n-1]-x[0])/float(n-1)
  sum2=h*(y[0]+y[n-1])/3.0
  for i in range(1,n-1):
    sum2+=h*y[i]*2.0*(1.0+mod(i,2))/3.0
  return sum1
  
from numpy import *            #best code
def simp(x,y):
  n=len(x)
  h=abs(x[n-1]-x[0])/float(n-1)
  c=(mod(range(n),2)+1)*2
  c[0]=1
  c[n-1]=1
  sum1=sum(h*c*y/3.0)
  return sum1


eg:

x=1.0*array(range(9))    #for integrating y from 0 to 8
y=x**2+2.0*x
print (simp(x,y),8**3/3.0+8**2)

"""