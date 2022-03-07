#-----
# Description   : Example script to use cpu backprojection code
# Date          : Nov 2020
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

#%% Start logging
import logging
logging.basicConfig(filename='exampleCpuBP.log', filemode='w', level=logging.INFO)
logging.info('  Script      "exampleCpuBP"      : exampleCpuBP.py')

#%% Import libraries
import os
import numpy as np
import matplotlib.pyplot as plt

# stop writing __pycache__ files
import sys
sys.dont_write_bytecode = True

from pyoat import *

#%% Data paths (defined by users)
folderPath          = 'data/rawData'
scanName            = 'mouseCrossSection'

#%% read signal file
oaData              = oaReader(folderPath=folderPath, scanName=scanName, averaging=False)
sigMat              = oaData.sigMat

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
imageRecon          = bp.reconBP(sigMat)

# #%% Visualize reconstructed images (optional)
# plt.figure()
# plt.imshow(imageRecon[:,:,0,0], cmap='gray')
# plt.show()

#%% Save reconstructed images (optional)

# save as png
imageReconRotated = np.rot90(imageRecon,1)
pngPath = 'data/pngImages'
saveImagePng(reconObject=bp, pngPath=pngPath, saveName='BP_'+scanName, imageRecon=imageReconRotated)

# save as mat
imageReconRotated = np.rot90(imageRecon,1)
matPath = 'data/matImages'
saveImageMat(reconObject=bp, matPath=matPath, saveName='BP_'+scanName, imageRecon=imageReconRotated)

