import matplotlib.pyplot as plt
from math import sqrt
def Graph():
    masX=[]
    masY=[]
    x = -5
    while x <= 6:
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
        masX.append(x)
        masY.append(y)
        x+=0.1

    return masX, masY

mas=Graph()
plt.plot(mas[0],mas[1])
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()