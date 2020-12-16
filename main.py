import csv
import math
import numpy as np
import matplotlib.pyplot as plt

import csv_import
import element
import f_matrix
import funcionts
import funcionts
import k_matrix

prop = []
nodes = []
elements = []
condU = []
condF  = []

variablesArray =[
    prop, #P_id;dens;E;v;A
    nodes,#N_id;x;y;;
    elements,#E_id;from;to;prop;
    condU,#I_U_id;N_id;u_x;u_y;
    condF#I_F_id;N_id;Fx;Fy;
]

csv_import.csv_toVar('Test4.csv',variablesArray)


e0 =  element.Element(0,prop,nodes,elements)
funcionts.fivePrec(e0.kElementMartix)
e0.printEr()

elementsContainer = []
element.elementsMaker(variablesArray,elementsContainer)


mxSize = len(variablesArray[1])*3
globalKMx = np.zeros((mxSize,mxSize))
print(globalKMx)
k_matrix.globalKMxMaker(globalKMx,elementsContainer)
funcionts.fivePrec(globalKMx)
print(globalKMx)



globalRedKMx = np.copy(globalKMx)
print(globalRedKMx)
gr = np.delete(globalRedKMx,[0,1],0) #<-- array, what i, row/coloum
gr2 = np.delete(gr,[0,1],1) #<-- array, what i, row/coloum

globalRedKMx = k_matrix.globalRedKMxMaker(globalRedKMx,variablesArray[3])
print(globalRedKMx)

fMx = f_matrix.initFToArrayMaker(mxSize,variablesArray[4])
print(fMx)

fMxRed = f_matrix.fTofRed(variablesArray[3],fMx)
print(fMxRed) #!!!!!!!!!!!!!NYOMaték

print(fMxRed)
print(globalRedKMx)


try1 = np.linalg.inv(globalRedKMx)
funcionts.fivePrec(try1)
try2 = np.multiply(fMxRed,try1)
try3 = try1*fMxRed
try4 = np.matmul(try1,fMxRed)
try5 = try1@fMxRed
print(try1)
#print(try2)
#print(try3)
#print(try4)
print(try5)