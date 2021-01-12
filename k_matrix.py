import numpy as np
import funcionts

# Gets
# Does
# Gives

def globalKMxMaker(kMx,elem):
    #print(len(elem[0].kElementMartix))
    for e in elem:
        for i in range(len(e.kElementMartix)):
            for j in range(len(e.kElementMartix)):
                #print(e.kElementMartix[i][j])
                n1 = e.nodeNum[i]
                n2 = e.nodeNum[j]
                #print(n1,n2)
                kMx[n1][n2] += e.kElementMartix[i][j]
                #print(kMx[n1][n2])
                #funcionts.printHelper("global K Matrix",kMx)

# Gets
# Does
# Gives

def globalRedKMxMaker(kMx,inU): # kiszedi az össze kitörlendő szart és egyszere törli
    hArray = []
    for init in inU:
        #funcionts.printHelper("bROOO",init)
        if int(init[2]) == 1:
            hArray.append(int(init[1])*3)
        if int(init[3]) == 1:
            hArray.append(int(init[1])*3+1)
        if int(init[4]) == 1:
            hArray.append(int(init[1])*3+2)
    h1 = np.delete(kMx,hArray,0)
    h2 = np.delete(h1,hArray,1)
    return np.copy(h2)