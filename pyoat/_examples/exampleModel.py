#-----
# Description   : Example script to create model matrix
# Date          : March 2022
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

#%% Start logging
import logging
logging.basicConfig(filename='exampleModel.log', filemode='w', level=logging.INFO)
logging.info('  Script      "exampleModel"     	: exampleModel.py')

#%% Import libraries
from scipy.sparse import save_npz, load_npz

# stop wiriting __pycache__ files
import sys
sys.dont_write_bytecode = True

from pyoat import *

#%% Initialize cpuMB object
mb                  = cpuMB()

#%% Reconstruction parameters (defined by user)
mb.speedOfSound     = 1535              # change SoS based on water temperature (default: 1480)
mb.fieldOfView      = 0.024             # FOV to reconstruct (default: 0.03)
mb.pixelNumber      = 512               # increase this number for higher resolution (default: 128)
mb.cupType          = 'ring'            # ring, multisegment, virtualRing (default: ringCup)
mb.delayInSamples   = 64              	# reception delay in samples
mb.regMethod        = None         		# for model matrix only, give None (only tikonov implemented so far)

#%% Calculate model matrix
# OPTION 1: Calculate model matrix
# WARNING: If you change parameters above, you need to calculate matrix again
# WARNING: If the parameters are the same model matrix can be used several times after calculating at the beginning 
modelMatrix         = mb.calculateModelMatrix()

# # OPTIONAL
# # save model matrix
save_npz('data/modelMatrices/pixel512.npz', modelMatrix)

# # OPTION 2: Load model matrix
# modelMatrix = load_npz('data/modelMatrices/pixel512.npz')
