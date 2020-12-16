import numpy as np

# Gets
# Does
# Gives

def globalKMxMaker(kMx,elem):
    print(len(elem[0].kElementMartix))
    for e in elem:
        for i in range(len(e.kElementMartix)):
            for j in range(len(e.kElementMartix)):
                #print(e.kElementMartix[i][j])
                n1 = e.nodeNum[i]
                n2 = e.nodeNum[j]
                #print(n1,n2)
                kMx[n1][n2] += e.kElementMartix[i][j]
                #print(kMx[n1][n2])

# Gets
# Does
# Gives

def globalRedKMxMaker(kMx,inU):
    hArray = []
    for init in inU:
        print(init)
        if int(init[2]) == 1:
            hArray.append(int(init[1])*2)
        if int(init[3]) == 1:
            hArray.append(int(init[1])*2+1)
    h1 = np.delete(kMx,hArray,0)
    h2 = np.delete(h1,hArray,1)
    return np.copy(h2)