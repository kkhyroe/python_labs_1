from math import *

def f1(a):
    y = (((sin(a))**4)+2*sin(a)*cos(a)-(cos(a))**4) / ((2*tan(a)) / (1-tan(a)**2))
    return y

def f2(a):
    y = cos(a)**2 - sin(a)**2
    return y

fo = open('output.txt', 'wt')
fi = open('input.txt', 'rt')
a = float(fi.readline())

fo.write(str(f1(a)))
fo.write('\n')
fo.write(str(f2(a)))
fo.close()
fi.close()
