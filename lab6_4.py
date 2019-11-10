from math import *
from random import *

fi = open('input.txt', 'rt')
fo = open('output.txt', 'wt')

a = []

n = int(fi.readline())
x0 = float(fi.readline())
y0 = float(fi.readline())
r = float(fi.readline())

for i in range(n):
    a.append(uniform(-5.0, 5.0))
    a.append(uniform(-5.0, 5.0))

dMax = 0
for i in range(0, n*2, 2):
    for j in range(i+2, n*2, 2):
        d = hypot(a[j]-a[i], a[j+1]-a[i+1])

        if d > dMax:
            dMax = d

fo.write('| Максимальное расстояние = ')
fo.write(str(dMax))
fo.write(' |\n')

b = []

for i in range(0, n*2, 2):
    d = hypot(x0-a[i], y0-a[i+1])
    if d <= r:
        b.append([a[i], a[i+1]])

fo.write('| Ко-ты точек, которые попадают в круг: ')
fo.write(str(b))
fo.write(' |\n')

c = []

for i in range(n):
    c.append([a[i], a[i+1]])

c = sorted(c, key=lambda x: x[0])

fo.write(str(c))

fi.close()
fo.close()
