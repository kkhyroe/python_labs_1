from math import *
from random import *

a = []

n = int(input('n = '))
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
r = float(input('r = '))

for i in range(n):
    a.append(uniform(-5.0, 5.0))
    a.append(uniform(-5.0, 5.0))

print(a)

dMax = 0
for i in range(0, n*2, 2):
    for j in range(i+2, n*2, 2):
        d = hypot(a[j]-a[i], a[j+1]-a[i+1])

        if d > dMax:
            dMax = d

print('| Максимальное расстояние =', dMax, '|')

b = []

for i in range(0, n*2, 2):
    d = hypot(x0-a[i], y0-a[i+1])
    if d <= r:
        b.append([a[i], a[i+1]])

print('| Ко-ты точек, которые попадают в круг:', b, '|')

c = []

for i in range(n):
    c.append([a[i], a[i+1]])

c = sorted(c, key=lambda x: x[0])

print(c)
