
def f(x):
  return x**2+2*x+1
  
w=[128/225,(322+13*(70)**0.52)/900,(322+13*(70)**0.52)/900,(322-13*(70)**0.5)/900,(322-13*(70)**0.5)/900]

z=[0,((5-2*(10/7)**0.5)**0.5)/3,-((5-2*(10/7)**0.5)**0.5)/3,((5+2*(10/7)**0.5)**0.5)/3,-((5+2*(10/7)**0.5)**0.5)/3]

def gquad(a,b,f,n=5):
  c=0
  t=(b-a)/2
  x=(b+a)/2
  for i in range(n):
    c+=w[i]*f(t*z[i]+x)
  return c*t

a=float(input('enter a:'))
b=float(input('enter b:'))

  
print('integral = ',gquad(a,b,f))