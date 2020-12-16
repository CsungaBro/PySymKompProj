import csv
import math
import numpy as np
import matplotlib.pyplot as plt


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

def dataRowCounter(data,name,dataTo):
    for i in range(len(data)):
        for j in range(len(name)):
            if data[i][0] == name[j]:
                dataTo[j] = i + 2
    dataTo[5] = len(data) + 2

def rangeMaker(ranges,rows): 
    for i in range(len(ranges)):
        ranges[i].append(rows[i])
        ranges[i].append(rows[i+1]-2)

def dataToArray(variab,rang,data):
    for i in range(len(variab)):
        h1 = rang[i][0]
        h2 = rang[i][1]
        for j in range(h1,h2):
            variab[i].append(data[j])


def arrayCleaner(array):
    for data in array:
        for row in data:
            h1 = []
            for i in range(len(row)):
                if row[i] == '':
                    h1.append(i)
            h1.reverse()
            for j in h1:
                del row[j]

def csv_toVar(csv_File,varArray):
    with open(csv_File, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =";")
        lines = [line for line in csv_reader]
    varNames=[
        "Prop",
        "Nodes",
        "Elements",
        "In_Conds_U",
        "In_Conds_F",
        "End"
    ]
    rowCounter = [
        0,#Prop
        0,#Nodes
        0,#Elements
        0,#In_Conds_U
        0,#In_Conds_F
        0,#End
    ]
    rangeCounter = [
        [],#PropRange:
        [],#NodesRange
        [],#ElementsRange
        [],#In_Conds_URange
        []#In_Conds_FRange
    ]
    dataRowCounter(lines,varNames,rowCounter)
    rangeMaker(rangeCounter,rowCounter)
    dataToArray(varArray,rangeCounter,lines)
    arrayCleaner(varArray)
    dataPrinter(varArray)


csv_toVar('Test.csv',variablesArray)


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
csv_toVar('Test2.csv',variablesArray)

class Element:
    def __init__(self,id_E,propert,node,element):
        elementRow = 0
        self.x = [0,0] 
        self.y = [0,0]

        for row in element:
          if int(row[0]) == id_E:
              elementRow = row

        for row in propert:
            if int(elementRow[3]) == int(row[0]):      
                self.dens = float(row[1])
                self.E = float(row[2])
                self.v = float(row[3])
                self.A = 1 #TODO implementation of A into csv
                #self.A = float(row[4])

        for row in node:
            if int(elementRow[1]) == int(row[0]):
                self.x[0] =float(row[1])
                self.y[0] =float(row[2])

        for row in node:
            if int(elementRow[2]) == int(row[0]):
                self.x[1] =float(row[1])
                self.y[1] =float(row[2])        

        self.L = math.sqrt((self.x[0]-self.x[1])**2+(self.y[0]-self.y[1])**2)

        if self.y[1]-self.y[0] == 0:
            if self.x[1]-self.x[0] > 0:
                self.alfa = 0*math.pi/180
            elif self.x[1]-self.x[0] < 0:
                self.alfa = 180*math.pi/180
        elif self.x[1]-self.x[0] == 0:
            if self.y[1]-self.y[0] > 0:
                self.alfa = 90*math.pi/180
            elif self.y[1]-self.y[0] < 0:
                self.alfa = 270*math.pi/180
        else:
            self.alfa = math.atan(self.y[1]-self.y[0])/(self.x[1]-self.x[0]) 

        self.kElementMartix = np.array([
            [math.cos(self.alfa)**2,math.cos(self.alfa)*math.cos(self.alfa),-math.cos(self.alfa)**2,-math.cos(self.alfa)*math.cos(self.alfa)],
            [math.cos(self.alfa)*math.cos(self.alfa),math.sin(self.alfa)**2,-math.cos(self.alfa)*math.cos(self.alfa),-math.sin(self.alfa)**2],
            [-math.cos(self.alfa)**2,-math.cos(self.alfa)*math.cos(self.alfa),math.cos(self.alfa)**2,math.cos(self.alfa)*math.cos(self.alfa)],
            [-math.cos(self.alfa)*math.cos(self.alfa),-math.sin(self.alfa)**2,math.cos(self.alfa)*math.cos(self.alfa),math.sin(self.alfa)**2]
            ])
        self.kElementMartix *=  (self.A*self.E/self.L)

    def printEr(self):
        print(self.x)
        print(self.y)
        print(self.dens)
        print(self.E)
        print(self.v)
        print(self.A)
        print(self.L)
        print(self.alfa)
        print(self.kElementMartix)

e0 =  Element(0,prop,nodes,elements)
e0.printEr()

def elementsMaker(array):
    elementsContainer = []
    for e in array[2]:
        elementsContainer.append(Element(0,array[0],array[1],array[2]))
    for x in elementsContainer:
        print(x.kElementMartix)

elementsMaker(variablesArray)

print(variablesArray[0])