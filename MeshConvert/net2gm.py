#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:13:33 2018

@author: FlyFox

convert the *.msh from netgen to gmsh format
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#######################################################
### Switch to current dir(the same as .py script)   ###
#######################################################
currentdir=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentdir)


filename='sample.msh'
newfilename='new_'+filename
inp=open(filename,'r')
out=open(newfilename,'w')

nNodes=0;nElmts=0

X=[];Y=[];Z=[]

line=inp.readline()
while len(line)>0:
    if '$MeshFormat' in line:
        out.write(line)
        # read 2.000000 0 8
        line=inp.readline()
        out.write(line)
        # read $EndMeshFormat
        line=inp.readline()
        out.write(line)
    elif '$Nodes' in line:
        out.write(line)
        # read node number
        line=inp.readline()
        out.write(line)
        nNodes=int(line)
        for i in range(nNodes):
            line=inp.readline()
            out.write(line)
            linevalue=line.split()
            X.append(float(linevalue[2-1]))
            Y.append(float(linevalue[3-1]))
            Z.append(float(linevalue[4-1]))
        # read $EndNodes
        line=inp.readline()
        out.write(line)
    elif '$Elements' in line:
        out.write(line)
        # read elmts number
        line=inp.readline()
        out.write(line)
        nElmts=int(line)
        for e in range(nElmts):
            line=inp.readline()
            linevalue=line.split()
            if len(linevalue)==8:
                # for 2D case
                out.write(line)
            elif len(linevalue)==9:
                # for 3D case
                newlinevalue=[]
                for i in range(5): 
                    newlinevalue.append(int(linevalue[i]))
                newlinevalue.append(int(linevalue[5+1-1])) # first node
                newlinevalue.append(int(linevalue[5+2-1])) # second node
                newlinevalue.append(int(linevalue[5+4-1])) # third node
                newlinevalue.append(int(linevalue[5+3-1])) # last node
                line=''
                for i in range(9):
                    line+='%g '%(newlinevalue[i])
                out.write(line)
        
        # read $EndElements
        line=inp.readline()
        out.write(line)
    line=inp.readline()

print('convert finished!')
print('Write *.msh to file=',newfilename)
inp.close()
out.close()

fig=plt.figure(1)
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X,Y,Z)
plt.savefig('sample.png',dpi=500,bbox_inch='tight')
plt.show()

        
