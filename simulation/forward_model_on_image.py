import logging
import numpy as np


def forward(inputImage, modelMatrix, number_of_samples=2030, autoResize=True):
    logging.info('  Function    "forward"      		: %s', __name__)

    num_element = int(np.shape(modelMatrix)[0] / number_of_samples)

    # pixel number in model matrix
    pixel_numberMatrix = int(np.sqrt(np.shape(modelMatrix)[1]))

    # pixel number in image
    pixel_numberImage = np.shape(inputImage)[0]

    # resize image
    if pixel_numberMatrix != pixel_numberImage:
        if autoResize:
            inputImage = np.resize(inputImage, (pixel_numberMatrix, pixel_numberMatrix))
        else:
            raise AssertionError('Sizes of image and model matrix do not match!')

    # flatten the image
    inputImage = np.array(inputImage)
    imageFlat = inputImage.flatten()

    # multiply with model matrix
    sigMatVec = modelMatrix * imageFlat
    sigMat = np.transpose(sigMatVec.reshape(num_element, -1))

    return sigMat

# Apply forward model on the given image
# inputImage: image to apply forward model
# modelMatrix: model to apply on the image
# number_of_samples: number of time points in acquisition
# autoResize: resize image to match model matrix size
# return signal matrix (sigMat)