from math import *

x = float(input())

if x < -4:
    y = 2
elif (x >= -4) and (x < -2):
   y = 2-(sqrt(4-((x+2)**2)))
elif (x >= -2) and (x <= 0):
    y = 0
elif (x > 0) and (x <= 3):
    y = -x
elif (x > 3) and (x < 5):
    y = sqrt(4-(x-3)**2) - 1
elif x >= 5:
    y = -1

print(x, y)
