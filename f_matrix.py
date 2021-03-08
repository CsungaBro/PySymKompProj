import numpy as np

# Gets
# Does
# Gives

def initFToArrayMaker(mxSize,inF):
    h1 = np.zeros((mxSize,1))

    for i in inF:
        for j in range(0,3):
            h1[int(i[1])*3+j][0] += int(i[2+j])
    return np.copy(h1)

# Gets
# Does
# Gives

def fTofRed(inU,array):
    hArray = []
    for init in inU:
        if int(init[2]) == 1:
            hArray.append(int(init[1])*3)
        if int(init[3]) == 1:
            hArray.append(int(init[1])*3+1)
        if int(init[4]) == 1:
            hArray.append(int(init[1])*3+2)
    h1 = np.delete(array,hArray,0)
    return np.copy(h1)
