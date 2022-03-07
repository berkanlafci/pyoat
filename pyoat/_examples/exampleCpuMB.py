#-----
# Description   : Example script to use cpu backprojection code
# Date          : Nov 2020
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

#%% Start logging
import logging
logging.basicConfig(filename='exampleCpuMB.log', filemode='w', level=logging.INFO)
logging.info('  Script      "exampleCpuMB"      : exampleCpuMB.py')

#%% Import libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import save_npz, load_npz

# stop wiriting __pycache__ files
import sys
sys.dont_write_bytecode = True

from pyoat import *

#%% Data paths (defined by users)
folderPath          = 'data/rawData'
scanName            = 'mouseCrossSection'

#%% read signal file
oaData              = oaReader(folderPath=folderPath, scanName=scanName, averaging=False)
sigMat              = oaData.sigMat

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
mb.regMethod        = 'tikonov'         # for model matrix only, give None (only tikonov implemented so far)
mb.lambdaReg 		= 0

#%% Calculate model matrix
# OPTION 1: Calculate model matrix
# WARNING: If you change parameters above, you need to calculate matrix again
# WARNING: If the parameters are the same model matrix can be used several times after calculating at the beginning 
modelMatrix         = mb.calculateModelMatrix()

# # OPTIONAL
# # save model matrix
# save_npz('data/modelMatrices/pixel512.npz', modelMatrix)

# # OPTION 2: Load model matrix
# modelMatrix = load_npz('data/modelMatrices/pixel512.npz')

#%% Calculate reconstruction matrix (model matrix + regularization matrix)
reconMatrix 		= mb.calculateReconMatrix(modelMatrix)

#%% Reconstruction
imageRecon          = mb.recon(sigMat, reconMatrix)

#%% Visualize reconstructed images (optional)
# plt.figure()
# plt.imshow(imageRecon, cmap='gray')
# plt.show()

#%% Save reconstructed images (optional)

# save as png
imageReconRotated = np.rot90(imageRecon,2)
imageReconFlipped = np.fliplr(imageReconRotated)
pngPath = 'data/pngImages'
saveImagePng(reconObject=mb, pngPath=pngPath, saveName='MB_'+scanName, imageRecon=imageReconFlipped)

# save as mat
imageReconRotated = np.rot90(imageRecon,2)
imageReconFlipped = np.fliplr(imageReconRotated)
matPath = 'data/matImages'
saveImageMat(reconObject=mb, matPath=matPath, saveName='MB_'+scanName, imageRecon=imageReconFlipped)
