#-----
# Description   : Example script to create model matrix
# Date          : March 2022
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

#%% Start logging
import logging

logging.basicConfig(filename='exampleForward.log', filemode='w', level=logging.INFO)
logging.info('  Script      "exampleForward"   	: exampleForward.py')

#%% Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import load_npz

# stop wiriting __pycache__ files
import sys
sys.dont_write_bytecode = True

# import pyoat library
from pyoat import *

# load model matrix
modelMatrix 	= load_npz('data/modelMatrices/pixel512.npz')

# define parameters for simulation image
pixelNumber 	= 512
rCircle 		= 50
centerCircle 	= 150

# create mesh
x               = np.linspace(0,pixelNumber-1,pixelNumber)
y               = np.linspace(0,pixelNumber-1,pixelNumber)
meshX, meshY    = np.meshgrid(x,y)

# apply position of circle
meshX_ 			= meshX - centerCircle
meshY_ 			= meshY - centerCircle

# create circle
inputImage 		= 1 - ((meshX_**2)/(rCircle**2) + (meshY_**2)/(rCircle**2))
inputImage[inputImage < 0] = 0

# create sub plots
fig, axes = plt.subplots(2, 2)

# show simulated image
ax = axes[0,0]
ax.imshow(inputImage, cmap='gray')
ax.axis('off')
ax.set_title('Input Image')

# apply forward model
sigMat = forward(inputImage, modelMatrix)

# show corresponding signals
ax = axes[0,1]
ax.imshow(sigMat, cmap='gray')
ax.axis('off')
ax.set_aspect(0.25)
ax.set_title('Signals')

#%% Initialize cpuBP object
bp                  = cpuBP()

#%% Reconstruction parameters (defined by user)
bp.speedOfSound     = 1535              # change SoS based on water temperature (default: 1480)
bp.fieldOfView      = 0.024             # FOV to reconstruct (default: 0.03)
bp.pixelNumber      = 512               # increase this number for higher resolution (default: 128)
bp.cupType          = 'ring'    		# ring, multisegment, virtualRing (default: ringCup)
bp.reconType        = 'full'            # full, direct or derivative (default: full)
bp.delayInSamples   = 64                # reception delay in samples
bp.wavelengths      = [800]             # wavelengths used in acquisition
bp.lowCutOff        = 0.1e6             # low cutoff for bandpass (default: 0.1e6)
bp.highCutOff       = 6e6               # high cutoff for bandpass (default: 6e6)

#%% Reconstruction
imageRecon          = bp.reconBP(-sigMat)

# show reconstructed image
ax = axes[1,0]
ax.imshow(imageRecon[:,:,0,0], cmap='gray')
ax.axis('off')
ax.set_title('Back Projection')

#%% Initialize cpuMB object
mb                  = cpuMB()

#%% Reconstruction parameters (defined by user)
mb.speedOfSound     = 1535              # change SoS based on water temperature (default: 1480)
mb.fieldOfView      = 0.024             # FOV to reconstruct (default: 0.03)
mb.pixelNumber      = 512               # increase this number for higher resolution (default: 128)
mb.cupType          = 'ring'            # ring, multisegment, virtualRing (default: ringCup)
mb.delayInSamples   = 64                # reception delay in samples
mb.wavelengths      = [800]             # wavelengths used in acquisition
mb.lowCutOff        = 0.1e6             # low cutoff for bandpass (default: 0.1e6)
mb.highCutOff       = 6e6               # high cutoff for bandpass (default: 6e6)
mb.iterationNum     = 5                 # iteration number for lsqr minimization
mb.regMethod        = None         		# for model matrix only, give None (only tikonov implemented so far)
mb.lambdaReg 		= 0

#%% Calculate reconstruction matrix (model matrix + regularization matrix)
reconMatrix 		= mb.calculateReconMatrix(modelMatrix)

#%% Reconstruction
imageRecon          = mb.recon(-sigMat, reconMatrix)

# show reconstructed image
ax = axes[1,1]
ax.imshow(imageRecon[:,:,0,0], cmap='gray')
ax.axis('off')
ax.set_title('Model Based')

# save figure
plt.savefig('data/pngImages/compareMethods.jpg')