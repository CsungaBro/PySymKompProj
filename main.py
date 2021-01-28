import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines

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
    csv_import.csv_toVar('2_ModVer_Dokumentation.csv',variablesArray)                            # it takes the csv file and import its into an array as ints


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
        x_values=[float(nodes[el1][1]), float(nodes[el2][1])]
        y_values=[float(nodes[el1][2]), float(nodes[el2][2])]
        ax.plot(x_values, y_values,'-k')

    #Constraints in x,y,r direction
    for x in range(len(nodes)):
        if int(condU[x][2])==1 and int(condU[x][3])!=1 and int(condU[x][4])!=1:
            ax.plot(float(nodes[x][1]),float(nodes[x][2]),'sg')
        if int(condU[x][2])!=1 and int(condU[x][3])==1 and int(condU[x][4])!=1:
            ax.plot(float(nodes[x][1]),float(nodes[x][2]),'pc')
        if int(condU[x][2])==1 and int(condU[x][3])==1 and int(condU[x][4])!=1:
            ax.plot(float(nodes[x][1]),float(nodes[x][2]),'Pm')
        if int(condU[x][2])==1 and int(condU[x][3])==1 and int(condU[x][4])==1:
            ax.plot(float(nodes[x][1]),float(nodes[x][2]),'*y')
        if int(condU[x][2])!=1 and int(condU[x][3])!=1 and int(condU[x][4])!=1:
            ax.plot(float(nodes[x][1]),float(nodes[x][2]),'ok')

    #Forces in "x" direction
    for j in range(len(condF)):
        if int(condF[j][2])<0:
            x_values=[int(nodes[int(condF[j][1])][1]), int(nodes[int(condF[j][1])][1])-10]#+int(condF[j][2])]
            y_values=[int(nodes[int(condF[j][1])][2]), int(nodes[int(condF[j][1])][2])]
            ax.plot(x_values, y_values,'r<-')
        if int(condF[j][2])>0:
            x_values=[int(nodes[int(condF[j][1])][1]), int(nodes[int(condF[j][1])][1])+10]#+int(condF[j][2])]
            y_values=[int(nodes[int(condF[j][1])][2]), int(nodes[int(condF[j][1])][2])]
            ax.plot(x_values, y_values,'r>-')

    #Forces in "y" direction
    for j in range(len(condF)):
        if int(condF[j][3])<0:
            x_values=[int(nodes[int(condF[j][1])][1]), int(nodes[int(condF[j][1])][1])]
            y_values=[int(nodes[int(condF[j][1])][2]), int(nodes[int(condF[j][1])][2])-10]#+int(condF[j][3])]
            ax.plot(x_values, y_values,'rv-')
        if int(condF[j][3])>0:
            x_values=[int(nodes[int(condF[j][1])][1]), int(nodes[int(condF[j][1])][1])]
            y_values=[int(nodes[int(condF[j][1])][2]), int(nodes[int(condF[j][1])][2])+10]#+int(condF[j][3])]
            ax.plot(x_values, y_values,'r^-')


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
    funcionts.printHelper("100B",100*B)

    C=A.astype(float)
    
    FixMatrix=np.add(100000*B,C)

    funcionts.printHelper("FixMatrix",FixMatrix)

    elma=int((len(elements)))
    for i in range(elma):
        el11=int(elements[i][1])
        el22=int(elements[i][2])
        x_values2=[float(FixMatrix[el11][0]), float(FixMatrix[el22][0])]
        y_values2=[float(FixMatrix[el11][1]), float(FixMatrix[el22][1])]
        ax.plot(x_values2, y_values2,'b')

        funcionts.printHelper("x_values2",x_values2)
        funcionts.printHelper("y_values2",y_values2)

    bl1 = mlines.Line2D([], [], color='black', marker='o',markersize=10, label='Original structure')
    bl2 = mlines.Line2D([], [], color='blue', marker='o',markersize=10, label='Deformed structure')
    bl3 = mlines.Line2D([], [], color='green', marker='s',markersize=10, label='x-direction blocked')
    bl4 = mlines.Line2D([], [], color='cyan', marker='p',markersize=10, label='y-direction blocked')
    bl5 = mlines.Line2D([], [], color='magenta', marker='P',markersize=10, label='x and y direction blocked')
    bl6 = mlines.Line2D([], [], color='yellow', marker='*',markersize=10, label='Rotation blocked')
    bl7 = mlines.Line2D([], [], color='red', marker='^',markersize=10, label='Force')
    plt.legend(handles=[bl1,bl2,bl3,bl4,bl5,bl6,bl7])
    funcionts.printHelper("try5",try5)

    plt.axis('equal')
    plt.show()
main()
