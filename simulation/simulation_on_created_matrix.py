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

folderPath = str(Path.cwd()) + "\\raw_data"
scanName = ''

# load model matrix
modelMatrix = load_npz(folderPath + "\\" + scanName + ".npz")

# define parameters for simulation image
pixel_number = 512
rCircle = 50
centerCircle = 150

# create mesh
x = np.linspace(0, pixel_number - 1, pixel_number)
y = np.linspace(0, pixel_number - 1, pixel_number)
meshX, meshY = np.meshgrid(x, y)

# apply position of circle
meshX_ = meshX - centerCircle
meshY_ = meshY - centerCircle

# create circle
inputImage = 1 - ((meshX_ ** 2) / (rCircle ** 2) + (meshY_ ** 2) / (rCircle ** 2))
inputImage[inputImage < 0] = 0

# create sub plots
fig, axes = plt.subplots(2, 2)

# show simulated image
ax = axes[0, 0]
ax.imshow(inputImage, cmap='gray')
ax.axis('off')
ax.set_title('Input Image')

# apply forward model
sigMat = forward(inputImage, modelMatrix)

# show corresponding signals
ax = axes[0, 1]
ax.imshow(sigMat, cmap='gray')
ax.axis('off')
ax.set_aspect(0.25)
ax.set_title('Signals')

# Initialize backprojection_object object
bp = backprojection_object()

# %% Reconstruction parameters
bp.speed_of_sound = 1535  # change SoS based on water temperature (default: 1480)
bp.field_of_view = 0.024  # FOV to reconstruct (default: 0.03)
bp.pixel_number = 512  # increase this number for higher resolution (default: 128)
bp.transducer_spatial_distribution = 'ring'  # ring, multisegment, virtualRing (default: ringCup)
bp.reconstruction_type = 'full'  # full, direct or derivative (default: full)
bp.delay_number_of_samples = 64  # reception delay in samples
bp.wavelengths = [800]  # wavelengths used in acquisition
bp.low_cutoff_frequency = 0.1e6  # low cutoff for bandpass (default: 0.1e6)
bp.high_cutoff_frequency = 6e6  # high cutoff for bandpass (default: 6e6)

# %% Reconstruction
reconstructed_image = bp.backprojection_reconstruction_function(-sigMat)

# show reconstructed image
ax = axes[1, 0]
ax.imshow(reconstructed_image[:, :, 0, 0], cmap='gray')
ax.axis('off')
ax.set_title('Back Projection')

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
reconMatrix = mb.calculateReconMatrix(modelMatrix)

# %% Reconstruction
reconstructed_image = mb.recon(-sigMat, reconMatrix)

# show reconstructed image
ax = axes[1, 1]
ax.imshow(reconstructed_image[:, :, 0, 0], cmap='gray')
ax.axis('off')
ax.set_title('Model Based')

# save figure
plt.savefig(folderPath + "\\" + 'compareMethods.jpg')
