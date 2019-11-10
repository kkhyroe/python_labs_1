import numpy as np

strs = np.array([['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']])

A = [[], [], [], [], [], []]

B = []
n = 10
k = 26
for i in range (6):

    for j in range(6):

        if (strs[1] != B) and (strs[0] != B):
            y = np.random.randint(low=1, high=3)
        elif not strs[0]:
            y = 2
        elif not strs[1]:
            y = 1

        if y == 1:
            x = np.random.randint(low=1, high=n+1)
            n = n - 1
            A[i].append(strs[0][x-1])
            strs[0].remove(strs[0][x-1])
        
        elif y == 2:
            x = np.random.randint(low=1, high=k+1)
            k = k - 1
            A[i].append(strs[1][x-1])
            strs[1].remove(strs[1][x-1])

strk = ''
n = np.random.randint(low=1, high=11)

for i in range(n):

    z = np.random.randint(low=0, high=6)
    s = ''

    for j in range(6):
        s = s + A[z][j]

    strk = strk + ' ' + s

fo = open('output.txt', 'wt')
fo.write(str(strk))
fo.close()
