import os
import h5py
import logging
import numpy as np
import PIL.Image as img
import scipy.io as sio


def saveImagePng(reconObject=None, pngPath=None, saveName=None, reconstructed_image=None):
    logging.info('  Function    "saveImagePng"      : %s', __name__)

    # loop through repetitions
    for repetition_counter in range(0, reconObject.numRepetitions):

        # loop through wavelengths
        for wavelength_counter in range(0, reconObject.wavelength_measure_number):

            maxValue = np.amax(reconstructed_image[:, :, wavelength_counter, repetition_counter])
            minValue = np.amin(reconstructed_image[:, :, wavelength_counter, repetition_counter])

            # normalize image
            normRecon = 255 * (reconstructed_image[:, :, wavelength_counter, repetition_counter] - minValue) / (maxValue - minValue)

            # convert to rgb
            arrayRecon = img.fromarray(normRecon)
            if arrayRecon.mode != 'RGB':
                rgbRecon = arrayRecon.convert('RGB')

            rgbRecon.save(pngPath + '/' + saveName + '_' + str(reconObject.wavelengths[wavelength_counter]) + '.jpg')

# Save images in png files
# pngPath: Folder path to save images
# saveName: Saving name for individual file
# reconstructed_image: Reconstructed image to save


def saveImageMat(reconObject=None, matPath=None, saveName=None, reconstructed_image=None):
    logging.info('  Function    "saveImageMat"      : %s', __name__)

    # loop trhorugh repetitions
    for repetition_counter in range(0, reconObject.numRepetitions):

        # loop through wavelengths
        for wavelength_counter in range(0, reconObject.wavelength_measure_number):
            imageDict = {"reconstructed_image": reconstructed_image[:, :, wavelength_counter, repetition_counter]}

            sio.savemat((matPath + '/' + saveName + '_' + str(reconObject.wavelengths[wavelength_counter]) + '.mat'), imageDict)

# Save images in mat files
# matPath: Folder path to save images
# saveName: Saving name for individual file
# reconstructed_image: Reconstructed image to save

def saveSignalPng(reconObject=None, pngPath=None, saveName=None, signalRecon=None):
    logging.info('  Function    "saveSignalPng"     : %s', __name__)

    # loop through wavelengths
    for wavelength_counter in range(0, reconObject.wavelength_measure_number):

        maxValue = np.amax(signalRecon[:, :, wavelength_counter])
        minValue = np.amin(signalRecon[:, :, wavelength_counter])

        # normalize image
        normRecon = 255 * (signalRecon[:, :, wavelength_counter] - minValue) / (maxValue - minValue)

        # convert to rgb
        arrayRecon = img.fromarray(normRecon)
        if arrayRecon.mode != 'RGB':
            rgbRecon = arrayRecon.convert('RGB')

        rgbRecon.save(pngPath + '/' + saveName + '_' + '.jpg')


# Save individual signals in png files
# pngPath: Folder path to save images
# saveName: Saving name for individual file
# signalRecon: Reconstructed image to save


def saveSignalMat(reconObject=None, matPath=None, saveName=None, signalRecon=None):
    logging.info('  Function    "saveSignalMat"     : %s', __name__)

    # loop through wavelengths
    for wavelength_counter in range(0, reconObject.wavelength_measure_number):
        imageDict = {"signalRecon": signalRecon[:, :, wavelength_counter]}

        sio.savemat((matPath + '/' + saveName + '.mat'), imageDict)

# Save individual signals in mat files
# pngPath: Folder path to save images
# saveName: Saving name for individual file
# signalRecon: Reconstructed image to save

def saveImageH5(h5Path=None, saveName=None, reconstructed_image=None):
    savePath = os.path.join(h5Path, saveName)
    data = {}

    with h5py.File(savePath, 'a', libver='latest') as h5File:
        data['reconstructed_image'] = h5File.create_dataset('reconstructed_image', data=reconstructed_image)

# Save individual signals in h5 files
# matPath: Folder path to save images
# saveName: Saving name for individual file
# signalRecon: Reconstructed image to save

