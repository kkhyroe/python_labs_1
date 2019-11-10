from math import *
a = float(input())
z1 = (((sin(a))**4)+2*sin(a)*cos(a)-(cos(a))**4) / ((2*tan(a)) / (1-tan(a)**2))
z2 = cos(a)**2 - sin(a)**2
print(z1, z2)
