from math import *
from random import *
flag = 0

R = float(input())

print(" R     X     Y       Res ")
print("-------------------------")

for i in range(10):
    x = uniform(-2*R, 2*R)
    y = uniform(-2*R, R)

    if (x > -R) and (y > -R) and (x <= 0) and (y <= 0):
        flag = 1

    x1 = x - R
    y1 = y - R
    h = sqrt(x1**2 + y1**2)
    if h <= R:
        flag = 0

    x1 = x + R
    y1 = y
    h = sqrt(x1**2 + y1**2)
    if (x >= 0) and (y >= 0) and (x <= R):
        flag = 1

    print(R, "{0: 7.2f} {1: 7.2f}".format(x, y), end=" ")
    if flag:
        print("Yes")
    else:
        print("No")
