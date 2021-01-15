import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


#Nodes
nd = np.array([[20.0, 20.0], [80.0, 20.0], [50.0, 60.0]]) 
fig = plt.figure()
ax = fig.add_subplot(111)
   
#Constraits
ux=[1,1,0]
uy=[1,1,0]
ur=[0,0,0]

#Constraints "x" direction
for x in range(len(nd)):
    if ux[x]==1:
        ax.add_patch(patches.Rectangle((nd[1,x]-2, nd[0,x]-1), 0.5, 2.0,color='black'))
        
#Constraints "y" direction
for y in range(len(nd)):
    if uy[y]==1:
        ax.add_patch(patches.Rectangle((nd[1,y]-1, nd[0,y]-2), 2.0, 0.5,color='black'))

#Constraints "r" direction
for r in range(len(nd)):
    if ur[r]==1:
        ax.add_patch(patches.Rectangle((nd[1,r]+1, nd[0,r]-1), 0.5, 2.0,color='black'))
        
#Elements
el=np.array([[1,3],[2,3]])
for i in range(len(el)):
    x_values=[nd[el[i,0]-1,0], nd[el[i,1]-1,0]]
    y_values=[nd[el[i,0]-1,1], nd[el[i,1]-1,1]]
    ax.plot(x_values, y_values,'k')
    
#Forces in "x" direction
fx=[0,-7,10]
for j in range(len(fx)):
    x_values=[nd[j,0], nd[j,0]+fx[j]]
    y_values=[nd[j,1], nd[j,1]]
    if fx[j]<0:
        ax.plot(x_values, y_values,'r<-')
    if fx[j]>=0:
        ax.plot(x_values, y_values,'r>-')
        
#Forces in "y" direction
fy=[6,0,-10]
for j in range(len(fx)):
    x_values=[nd[j,0], nd[j,0]]
    y_values=[nd[j,1], nd[j,1]+fy[j]]
    if fy[j]<0:
        ax.plot(x_values, y_values,'rv-')
    if fy[j]>=0:
        ax.plot(x_values, y_values,'r^-')
plt.show()