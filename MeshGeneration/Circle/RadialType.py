#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:13:33 2018

@author: FlyFox

Mesh generation for circular type domain with multiple grains in radial way
"""

import os
import numpy as np
import matplotlib.pyplot as plt

#######################################################
### Switch to current dir(the same as .py script)   ###
#######################################################
currentdir=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentdir)

geofilename='radial.geo'
dx=0.25
print('*** Now we are in:',os.getcwd())


########################################################
### Parameters for radial type mesh generation       ###
########################################################
radius0=2.5     # inner grain's radius(one single grain in the core)
radius1=8.0     # the radius of the whole secondary particles
nGBs=8         # number of grains for each layer
MisMatch=False  # MisMatch=Flase(default->for a gradient change), True(->mismatch between layers)
nLayers=4       # number of layers(since the core is the first layer, so you will have at least two layers)

MisMatchTheta=30.0*(np.pi/180.0)
shiftangle=5.0*(np.pi/180.0)

intervals=10    # the number of points for each arc

LayerNodes=[];LayerNodesIntervalNodes=[]  # index by layer
MainNodeIndex=[];NodesIntervalIndex=[]    # index by layer
######################################################
### Generate the main nodes for each layer         ###
######################################################
for layer in range(nLayers):
    radiusi=radius0+layer*(radius1-radius0)/(nLayers-1)
    NodeCoords=np.empty(shape=[0,3])
    IntervalNodeCoords=np.empty(shape=[0,3])
    theta=2.0*np.pi/(nGBs)
    for i in range(nGBs):
        x=radiusi*np.cos(i*theta+shiftangle)
        y=radiusi*np.sin(i*theta+shiftangle)
        NodeCoords=np.append(NodeCoords,[[x,y,0.0]],axis=0)
        # for interval nodes
        alpha=theta/intervals
        theta1=i*theta
        for j in range(intervals-1):
            x=radiusi*np.cos(theta1+(j+1)*alpha+shiftangle)
            y=radiusi*np.sin(theta1+(j+1)*alpha+shiftangle)
            IntervalNodeCoords=np.append(IntervalNodeCoords,[[x,y,0.0]],axis=0)
    LayerNodes.append(NodeCoords)
    LayerNodesIntervalNodes.append(IntervalNodeCoords)



############################################
### output to the geo file
############################################
inp=open(geofilename,'w+')
str='dx=%.2f;\n'%(dx)
inp.write(str)

### out put all the node coords
nPoints=0
for layer in range(nLayers):
    coords=LayerNodes[layer]
    for i in range(len(coords)):
        x=coords[i,0]
        y=coords[i,1]
        nPoints+=1
        str='Point(%6d)={%14.6e,%14.6e,0.0,dx};\n'%(nPoints,x,y)
        inp.write(str)
### output all the interval node coords
nIntervalPoints=0
for layer in range(nLayers):
    coords=LayerNodesIntervalNodes[layer]
    for i in range(len(coords)):
        x=coords[i,0]
        y=coords[i,1]
        nIntervalPoints+=1
        str='Point(%6d)={%14.6e,%14.6e,0.0,dx};\n'%(nPoints+nIntervalPoints,x,y)
        inp.write(str)
### output the connectivity information
### for all the circles of eac layer
nLines=0
for layer in range(nLayers):
    for i in range(nGBs):
        nLines+=1
        str='Line(%d)={'%(nLines)
        # for main node
        str+='%d,'%(layer*nGBs+i+1)
        for j in range(intervals-1):
            str+='%d,'%(nPoints+layer*nGBs*(intervals-1)+i*(intervals-1)+j+1)
        if i==nGBs-1:
            str+='%d};\n'%(layer*nGBs+1)
        else:
            str+='%d};\n\n'%(layer*nGBs+i+2)
        inp.write(str)
##############################################################
### output the connectivity information between main node  ###
##############################################################
nMainNodeLines=0
for layer in range(nLayers-1):
    for i in range(nGBs):
        nMainNodeLines+=1
        i1=layer*nGBs+i+1
        i2=i1+nGBs
        str='Line(%d)={%d,%d};\n\n'%(nLines+nMainNodeLines,i1,i2)
        inp.write(str)

###############################################################
### output the surface information
nSurface=0
for layer in range(nLayers):
    if layer==0:
        # for core-surface
        nSurface+=1
        str='Line Loop(%d)={'%(nSurface)
        for i in range(nGBs-1):
            str+='%d,'%(layer*nGBs+i+1)
        str+='%d};\n'%(layer*nGBs+nGBs)
        str+='Plane Surface(%d)={%d};\n\n'%(nSurface,nSurface)
        inp.write(str)
    else:
        for i in range(nGBs):
            nSurface+=1
            str='Line Loop(%d)={'%(nSurface)
            # for inner interval node line loop
            ind0=(layer-1)*nGBs+i+1 # inner interval line
            str+='%d,'%(ind0)
            ind=nLines+(layer-1)*nGBs+i+1+1 # first main node line
            if i==nGBs-1:
                ind=nLines+(layer-1)*nGBs+1 # first main node line
            str+='%d,'%(ind)
            ind=layer*nGBs+i+1
            str+='%d,'%(ind*-1) # outer interval line
            ind=nLines+(layer-1)*nGBs+i+1 # second main node line
            str+='%d};\n'%(ind*-1)
            str+='Plane Surface(%d)={%d};\n\n'%(nSurface,nSurface)
            inp.write(str)

for i in range(nSurface):
    str='Physical Surface(%d)={%d};\n\n'%(i+1,i+1)
    inp.write(str)




inp.close()
print('*** Write to file:',geofilename)    
print('*** Number of grains=%g'%(nSurface))
print('*** Layers=%g, grains each layer=%g/1'%(nLayers,nGBs))

######################################################
### For visualization                              ###
######################################################
for layer in range(nLayers):
    coords=LayerNodes[layer]
    plt.plot(coords[:,0],coords[:,1])
    coords=LayerNodesIntervalNodes[layer]
    plt.plot(coords[:,0],coords[:,1])
plt.axis('equal')
plt.show()



