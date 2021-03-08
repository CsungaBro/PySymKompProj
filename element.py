import funcionts
import math
import numpy as np

# Gets
# Does
# Gives

def transMx(ang):
    c = math.cos(ang)        
    s = math.sin(ang)
    cs = c*s
    c2 = c**2
    s2 = s**2
    tMx = np.array([
        [c,s,0,0,0,0],
        [-s,c,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,c,s,0],
        [0,0,0,-s,c,0],
        [0,0,0,0,0,1]
    ])
    tMxT = np.transpose(tMx)
    return tMx,tMxT 

# Gets
# Does
# Gives

def kCompCalc(L,E,A,Iz):
    g = Iz*E/L**3
    h1 = np.array([
        [A*E/L,0,0,-A*E/L,0,0],
        [0,12*g,6*L*g,0,-12*g,6*L*g],
        [0,6*L*g,4*L**2*g,0,-6*L*g,2*L**2*g],
        [-A*E/L,0,0,A*E/L,0,0],
        [0,-12*g,-6*L*g,0,12*g,-6*L*g],
        [0,6*L*g,2*L**2*g,0,-6*L*g,4*L**2*g]
    ])
    return h1

# Gets
# Does
# Gives

class Element:
    def __init__(self,id_E,propert,node,element):
        id_E = int(id_E)
        elementRow = 0
        self.x = [0,0] 
        self.y = [0,0]  #EZ
        self.phi = [0,0]

        for row in element:
          if int(row[0]) == id_E:
              elementRow = row

        self.nodeNum =[ # EZ
         int(elementRow[1])*3,
         int(elementRow[1])*3+1,
         int(elementRow[1])*3+2,
         int(elementRow[2])*3,
         int(elementRow[2])*3+1,
         int(elementRow[2])*3+2
        ]
            

        for row in propert:
            if int(elementRow[3]) == int(row[0]):      
                self.dens = float(row[1])
                self.E = float(row[2])
                self.v = float(row[3])
                self.A = float(row[4]) 
                self.Iz = float(row[5])

        for row in node: # EZ
            if int(elementRow[1]) == int(row[0]):
                self.x[0] =float(row[1])
                self.y[0] =float(row[2])
                # self.phi[0] = float(row[3])

        for row in node:# EZ
            if int(elementRow[2]) == int(row[0]):
                self.x[1] =float(row[1])
                self.y[1] =float(row[2])
                # self.phi[1] = float(row[3])

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
            dyt = self.y[1]-self.y[0]
            dxt = self.x[1]-self.x[0]
            dtt = dyt/dxt
            self.alfa = math.atan(dtt) #TEST to greater than 180


        #c = math.cos(self.alfa)
        #s = math.sin(self.alfa)

        # self.kElementMartix = np.array([
        #     [c**2,c*s,-c**2,-c*s],
        #     [c*s,s**2,-c*s,-s**2],
        #     [-c**2,-c*s,c**2,c*s],
        #     [-c*s,-s**2,c*s,s**2]
        #     ])
        # self.kElementMartix *=  (self.A*self.E/self.L)
        tMx,tMxT = transMx(self.alfa)
        #print(tMx)
        #print(tMxT)  
        self.kElementMartix = tMxT @ kCompCalc(self.L,self.E,self.A,self.Iz) @ tMx
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
        print(self.nodeNum)

# Gets
# Does
# Gives

def elementsMaker(array,eContainer):
    for e in array[2]:
        eContainer.append(Element(e[0],array[0],array[1],array[2]))
    for x in eContainer:
        funcionts.fivePrec(x.kElementMartix)
        #print(x.kElementMartix)



