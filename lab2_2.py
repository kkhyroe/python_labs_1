from math import *

x = float(input())

y = float(input())

R = float(input())

j = 0

if (x > -R) and (y > -R) and (x <= 0) and (y <= 0):
    j = 1

x1 = x - R
y1 = y - R
h = sqrt(x1**2 + y1**2)
if h <= R:
    j = 0

x1 = x + R
y1 = y
h = sqrt(x1**2 + y1**2)
if (x >= 0) and (y >= 0) and (x <= R):
    j = 1

if j == 1:
    print('Попадает')
else:
    print('Не попадает')
