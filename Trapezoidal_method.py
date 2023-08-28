#to evaluate integral by dividing into trapeziums

def f(x):
  return x**2+2*x+1

def trapezoid(a,b,n,f):
  x0=a
  h=(b-a)/n
  x=a+h
  c=0
  for i in range(n):
    if x<=b:
      c+=0.5*h*(f(x0)+f(x))
      x0=x
      x+=h
  return c

a=float(input('enter a:'))
b=float(input('enter b:'))
n=int(input('enter no. of steps:'))
  
print('integral = ',trapezoid(a,b,n,f),0.5*(b-a)*(f(a)+f(b)))
