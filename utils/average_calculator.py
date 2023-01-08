import logging
import time
import numpy as np


def averageSignals(sigMat, axis=2):
    logging.info('  Function    "averageSignals"    : %s', __name__)
    print('***** averaging *****')
    startTime = time.time()

    sig_mat_average = np.sum(sigMat, axis=axis)

    endTime = time.time()
    print('time elapsed: %.2f' % (endTime - startTime))
    return sig_mat_average

# function average sigMat channels
# sigMat: Signal array
# axis: Averaging axis of array
# return Averaged signal values
# the #2 axis of the sigMat is the collected signal
