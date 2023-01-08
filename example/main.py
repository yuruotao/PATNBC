import logging
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
from patnbc import *
from pathlib import Path

logging.basicConfig(filename='photoacoustic_imaging.log', filemode='w', level=logging.INFO)
logging.info('  Script      "acoustic imaging using backprojection"      : main1.py')

sys.dont_write_bytecode = True

folderPath_root = str(Path.cwd()).strip("example")
folderPath = folderPath_root + "raw_data"
scanName = 'raw_data'

# read signal file
raw_data = photoacoustic_data_reader(folderPath=folderPath, scanName=scanName, averaging=False)
sigMat = raw_data.sigMat

# Initialize the backprojection_object
bp = backprojection_object()

# Reconstruction parameters
bp.speed_of_sound = 1535  # change SoS based on water temperature (default: 1480)
bp.field_of_view = 0.024  # FOV to reconstruct (default: 0.03)
bp.pixel_number = 512  # increase this number for higher resolution (default: 128)
bp.transducer_spatial_distribution = 'ring'  # ring, multisegment, virtualRing (default: ringCup)
bp.reconstruction_type = 'full'  # full, direct or derivative (default: full)
bp.delay_number_of_samples = 64  # reception delay in samples
bp.wavelengths = [800]  # wavelengths used in acquisition
bp.low_cutoff_frequency = 0.1e6  # low cutoff for bandpass (default: 0.1e6)
bp.high_cutoff_frequency = 6e6  # high cutoff for bandpass (default: 6e6)

# Reconstruction
reconstructed_image = bp.backprojection_reconstruction_function(sigMat)

# Visualize reconstructed images
plt.figure()
plt.imshow(reconstructed_image[:, :, 0, 0], cmap='gray')
# plt.show() to see the image

reconstructed_imageRotated = np.rot90(reconstructed_image, 1)

# save reconstructed images as png
pngPath = folderPath_root + 'result\\figure'
saveImagePng(reconObject=bp, pngPath=pngPath, saveName='BackProjection_fig',
             reconstructed_image=reconstructed_imageRotated)

# as mat
matPath = folderPath_root + 'result\\figure'
saveImageMat(reconObject=bp, matPath=matPath, saveName='BackProjection_fig',
             reconstructed_image=reconstructed_imageRotated)
