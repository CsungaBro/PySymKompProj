import numpy as np

def initFToArrayMaker(mxSize,inF):
    h1 = np.zeros((mxSize,1))

    for i in inF:
        for j in range(0,2):
            h1[int(i[1])*2+j][0] = int(i[2+j])
    return np.copy(h1)

def fTofRed(inU,array):
    hArray = []
    for init in inU:
        print(init)
        if int(init[2]) == 1:
            hArray.append(int(init[1])*2)
        if int(init[3]) == 1:
            hArray.append(int(init[1])*2+1)
    h1 = np.delete(array,hArray,0)
    return np.copy(h1)