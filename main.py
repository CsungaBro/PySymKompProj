import csv
import math
import numpy as np
import matplotlib.pyplot as plt

import csv_import
import element
import f_matrix
import funcionts
import graphic_test
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

def main():
    csv_import.csv_toVar('Test4.csv',variablesArray)                            # it takes the csv file and import its into an array as ints


    e0 =  element.Element(0,prop,nodes,elements)                                # Test
    funcionts.fivePrec(e0.kElementMartix)                                       # Test
    e0.printEr()                                                                # Test

    elementsContainer = []                                                      # contains all the ellement
    element.elementsMaker(variablesArray,elementsContainer)                     # makes the elements from the data's


    mxSize = len(variablesArray[1])*3 #TODO                                     # It gives the size of the K matrix
    globalKMx = np.zeros((mxSize,mxSize))                                       # makes a nxn zero matrix
    funcionts.printHelper("global K Matrix",globalKMx)                          # Test
    k_matrix.globalKMxMaker(globalKMx,elementsContainer)                        # it makes the global K matrix form the elements
    funcionts.fivePrec(globalKMx)                                               # it makes the valus display for the 5th value
    funcionts.printHelper("global K Matrix",globalKMx)                          # Test



    globalRedKMx = np.copy(globalKMx)                                           # makes a copy of the global K Matrix
    funcionts.printHelper("global K Red Matrix",globalRedKMx)                   # test
    gr = np.delete(globalRedKMx,[0,1],0)#<-- array, what i, row/coloum          ## Test 
    gr2 = np.delete(gr,[0,1],1)  #<-- array, what i, row/coloum                 ## Test 

    globalRedKMx = k_matrix.globalRedKMxMaker(globalRedKMx,variablesArray[3])   # makes the reducted K matrix from the global and the Initial U cond
    funcionts.printHelper("globalRedKMx", globalRedKMx,)                        # Test

    fMx = f_matrix.initFToArrayMaker(mxSize,variablesArray[4])                  # makes a nx1 matrix/vector from the array F
    funcionts.printHelper("F matrix",fMx)                                       # Test

    fMxRed = f_matrix.fTofRed(variablesArray[3],fMx)                            # Test
    funcionts.printHelper("F Red matrix",fMxRed) #TODO                          # NYOMaték #Test

    funcionts.printHelper("F Red matrix",fMxRed)                                # Test
    funcionts.printHelper("K Red Matrix",globalRedKMx)                          # Test

    

    try1 = np.linalg.inv(globalRedKMx)                                          # Inverz
    funcionts.fivePrec(try1)                                                    # it makes the valus display for the 5th value 
    try2 = np.multiply(fMxRed,try1)                                             # try mult
    try3 = try1*fMxRed                                                          # try multi
    try4 = np.matmul(try1,fMxRed)                                               # try multi
    try5 = try1@fMxRed                                                          # try multi
    funcionts.printHelper("try1",try1)                                          # Test
    #print(try2)
    #print(try3)
    #print(try4)
    funcionts.printHelper("try5",try5)                                          # Test

main()