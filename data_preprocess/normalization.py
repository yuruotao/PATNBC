import logging
import time
import numpy as np


def sig_mat_normalization(sigMatIn):
    logging.info('  Function    "sig_mat_normalization"   : %s', __name__)

    print('***** normalization *****')
    startTime = time.time()

    sigMatOut = np.zeros(np.shape(sigMatIn))

    for i in range(np.shape(sigMatIn)[2]):
        singleF = sigMatIn[:, :, i]
        meanF = np.mean(singleF, axis=0)
        sigMatOut[:, :, i] = singleF - np.tile(meanF, (np.shape(singleF)[0], 1))

    endTime = time.time()
    print('time elapsed: %.2f' % (endTime - startTime))

    return sigMatOut

# Band pass filtering for signals
# sigMatIn: 3D array (samples x channels x repetition) of signals
# return: 3D array normalized around mean value of the channels