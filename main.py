import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    csv_import.csv_toVar('Test6.csv',variablesArray)                            # it takes the csv file and import its into an array as ints


    e0 =  element.Element(0,prop,nodes,elements)                                # Test
    funcionts.fivePrec(e0.kElementMartix)                                       # Test
    e0.printEr()                                                                # Test

    elementsContainer = []                                                      # contains all the ellement
    element.elementsMaker(variablesArray,elementsContainer)                     # makes the elements from the data's
    funcionts.printHelper("nodes",nodes)
    funcionts.printHelper("elements",elements)
    funcionts.printHelper("len(elements)",len(elements))
    funcionts.printHelper("CondU",condU)
    funcionts.printHelper("len(nodes)",len(nodes))
    #Visualization of the input

    #Elements
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    elmo=int((len(elements)))
    for i in range(elmo):
        el1=int(elements[i][1])
        el2=int(elements[i][2])
        x_values=[int(nodes[el1][1]), int(nodes[el2][1])]
        y_values=[int(nodes[el1][2]), int(nodes[el2][2])]
        ax.plot(x_values, y_values,'k')

    #Constraints in x direction
    for x in range(len(nodes)):
        if int(condU[x][2])==1:
            Constx=patches.Rectangle((int(nodes[x][1])-2,int(nodes[x][2])-3),4,1,color='black')
            ax.add_patch(Constx)
            
    #Constraints in y direction
    for x in range(len(nodes)):
        if int(condU[x][3])==1:
            Constx=patches.Rectangle((int(nodes[x][1])-3,int(nodes[x][2])-2),1,4,color='black')
            ax.add_patch(Constx)

    #Rotational constraint
    for x in range(len(nodes)):
        if int(condU[x][4])==1:
            Constx=patches.Rectangle((int(nodes[x][1])+2,int(nodes[x][2])-2),1,4,color='black')
            ax.add_patch(Constx)

    #Forces in "x" direction
    for j in range(len(condF)):
        x_values=[int(nodes[int(condF[j][1])][1]), int(nodes[int(condF[j][1])][1])+int(condF[j][2])]
        y_values=[int(nodes[int(condF[j][1])][2]), int(nodes[int(condF[j][1])][2])]
        if int(condF[j][2])<0:
            ax.plot(x_values, y_values,'r<-')
        if int(condF[j][2])>=0:
             ax.plot(x_values, y_values,'r>-')

    #Forces in "y" direction
    for j in range(len(condF)):
        x_values=[int(nodes[int(condF[j][1])][1]), int(nodes[int(condF[j][1])][1])]
        y_values=[int(nodes[int(condF[j][1])][2]), int(nodes[int(condF[j][1])][2])+int(condF[j][3])]
        if int(condF[j][3])<0:
            ax.plot(x_values, y_values,'rv-')
        if int(condF[j][3])>=0:
             ax.plot(x_values, y_values,'r^-')

    #Nodes
    for k in range(len(nodes)):
        Crc=patches.Circle((int(nodes[k][1]), int(nodes[k][2])), 1, color='red')
        ax.add_patch(Crc)   

    


    mxSize = len(variablesArray[1])*3 #TODO  implement as DOF                   # It gives the size of the K matrix
    globalKMx = np.zeros((mxSize,mxSize))                                       # makes a nxn zero matrix
    funcionts.printHelper("global K Matrix",globalKMx)                          # Test
    k_matrix.globalKMxMaker(globalKMx,elementsContainer)                        # it makes the global K matrix form the elements
    funcionts.fivePrec(globalKMx)                                               # it makes the valus display for the 5th value
    funcionts.printHelper("global K Matrix",globalKMx)                          # Test



    globalRedKMx = np.copy(globalKMx)                                           # makes a copy of the global K Matrix
    funcionts.printHelper("global K Red Matrix",globalRedKMx)                   # test
    # gr = np.delete(globalRedKMx,[0,1],0)#<-- array, what i, row/coloum        ## Test 
    # gr2 = np.delete(gr,[0,1],1)  #<-- array, what i, row/coloum               ## Test 

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
    #try2 = np.multiply(fMxRed,try1)                                             # try mult
    #try3 = try1*fMxRed                                                          # try multi
    #try4 = np.matmul(try1,fMxRed)                                               # try multi
    try5 = try1@fMxRed                                                          # try multi
    funcionts.printHelper("try1",try1)                                          # Test
    #print(try2)
    #print(try3)
    #print(try4)
    #funcionts.printHelper("try2",try2)                                          # Test
    #funcionts.printHelper("try3",try3)                                          # Test
    #funcionts.printHelper("try4",try4)                                          # Test
    funcionts.printHelper("try5",try5) 
    
    nArray = []
    for init in condU:
        
        if int(init[2]) == 1:
            nArray.append(int(init[1])*3)
        if int(init[3]) == 1:
            nArray.append(int(init[1])*3+1)
        if int(init[4]) == 1:
            nArray.append(int(init[1])*3+2)  
                                                   
    funcionts.printHelper("nArray",nArray)
    funcionts.printHelper("len(nodes)",len(nodes))

    FullMatrix=[]
    kszam=(int(len(nodes)))*3
    for z in range(kszam):
        FullMatrix.append(z)

    funcionts.printHelper("kszam",kszam)      
    funcionts.printHelper("FullMatrix",FullMatrix)

    MatDiff=(list(list(set(FullMatrix)-set(nArray)) + list(set(nArray)-set(FullMatrix))))
    funcionts.printHelper("MatDiff",MatDiff)

    ZeroMatrix=[]
    zszam=(int(len(nodes)))*3
    for z in range(zszam):
        ZeroMatrix.append(0)

    for l in range(len(MatDiff)):
        ZeroMatrix[MatDiff[l]]=try5[l][0]

    funcionts.printHelper("ZeroMatrix",ZeroMatrix)

    MovementMatrix = np.array(ZeroMatrix)
    HP=MovementMatrix.reshape(int(len(nodes)),3)

    funcionts.printHelper("HP",HP)        

    NodesMod=np.array(nodes)
    funcionts.printHelper("NodesMod",NodesMod)

    A=np.delete(NodesMod, 0, axis=1)
    B=np.delete(HP, 2, axis=1)
    
    funcionts.printHelper("A",A)
    funcionts.printHelper("B",B)
plt.show()
main()
