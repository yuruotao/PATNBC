import logging
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import load_npz
import sys
from patnbc import *
from pathlib import Path

logging.basicConfig(filename='forward_imaging.log', filemode='w', level=logging.INFO)
logging.info('  Script      "photoacoustic tomography using forward imaging"   	: forward_imaging_main.py')

sys.dont_write_bytecode = True

folderPath = str(Path.cwd()).strip("simulation") + "raw_data"
scanName = 'raw_data'

# read signal file
raw_data = photoacoustic_data_reader(folderPath=folderPath, scanName=scanName, averaging=False)
sigMat = raw_data.sigMat

# %% Initialize model_based_reconstruction object
mb = model_based_reconstruction()

# %% Reconstruction parameters
mb.speed_of_sound = 1535  # change SoS based on water temperature (default: 1480)
mb.field_of_view = 0.024  # FOV to reconstruct (default: 0.03)
mb.pixel_number = 100  # increase this number for higher resolution (default: 128)
mb.transducer_spatial_distribution = 'ring'  # ring, multisegment, virtualRing (default: ringCup)
mb.delay_number_of_samples = 64  # reception delay in samples
mb.wavelengths = [800]  # wavelengths used in acquisition
mb.low_cutoff_frequency = 0.1e6  # low cutoff for bandpass (default: 0.1e6)
mb.high_cutoff_frequency = 6e6  # high cutoff for bandpass (default: 6e6)
mb.iterationNum = 5  # iteration number for lsqr minimization
mb.regMethod = None  # for model matrix only, give None (only tikonov implemented so far)
mb.lambdaReg = 0

# %% Calculate reconstruction matrix (model matrix + regularization matrix)
reconMatrix = mb.calculateReconMatrix(sigMat)

# %% Reconstruction
reconstructed_image = mb.recon(-sigMat, reconMatrix)

# Visualize reconstructed images
plt.figure()
plt.imshow(reconstructed_image[:, :, 0, 0], cmap='gray')
# plt.show() to see the image

# save reconstructed images as png
reconstructed_imageRotated = np.rot90(reconstructed_image, 1)
pngPath = 'result/figure/pngImages'
saveImagePng(reconObject=mb, pngPath=pngPath, saveName='MB_' + scanName, reconstructed_image=reconstructed_imageRotated)

# as mat
matPath = 'result/figure/matImages'
saveImageMat(reconObject=mb, matPath=matPath, saveName='MB_' + scanName, reconstructed_image=reconstructed_imageRotated)
