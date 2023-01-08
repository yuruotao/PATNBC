import logging
from scipy.sparse import save_npz, load_npz
import sys
from patnbc import *
from pathlib import Path

logging.basicConfig(filename='model matrix creation.log', filemode='w', level=logging.INFO)
logging.info('  Script      "model matrix creation"     	: model_matrix_creation.py')
sys.dont_write_bytecode = True

folderPath = str(Path.cwd()).strip("simulation") + "raw_data"
print(folderPath)

# Initialize model_based_reconstruction object
mb = model_based_reconstruction()

# Reconstruction parameters
mb.speed_of_sound = 1535  # change SoS based on water temperature (default: 1480)
mb.field_of_view = 0.024  # FOV to reconstruct (default: 0.03)
mb.pixel_number = 512  # increase this number for higher resolution (default: 128)
mb.transducer_spatial_distribution = 'ring'  # ring, multisegment, virtualRing (default: ring)
mb.delay_number_of_samples = 64  # reception delay in samples
mb.regMethod = None # for model matrix only

# Calculate the model matrix
model_matrix = mb.calculateModelMatrix()

# save model matrix
save_npz(folderPath , model_matrix)

# model_matrix = load_npz('data/modelMatrices/pixel512.npz')
# load the existing model matrix