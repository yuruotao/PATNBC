import logging
import time
import numpy as np
from scipy.signal import butter, filtfilt


def sigMatFilter(sigMat, low_cutoff_frequency=0.1e6, high_cutoff_frequency=6e6, sampling_frequency=40e6, butterworth_filter_order=3, conRatio=0.5):
    logging.info('  Function    "sigMatFilter"      : %s', __name__)

    print('***** filtering *****')
    startTime = time.time()

    sigMatF = np.zeros(np.shape(sigMat))

    nyquistRatio = conRatio * sampling_frequency
    low_cutoff_frequency = low_cutoff_frequency / nyquistRatio
    high_cutoff_frequency = high_cutoff_frequency / nyquistRatio
    lowF, highF = butter(butterworth_filter_order, [low_cutoff_frequency, high_cutoff_frequency], btype='bandpass')

    sigMatF = filtfilt(lowF, highF, sigMat, padlen=0, axis=0)

    endTime = time.time()
    print('time elapsed: %.2f' % (endTime - startTime))

    return sigMatF


# sigMat: 3D array (samples x channels x repetition) of signals
# low_cutoff_frequency: Low cut off frequency of bandpass filter
# high_cutoff_frequency: High cut off frequency of bandpass filter
# sampling_frequency: Sampling frequency of signals
# butterworth_filter_order: Butterworth filter order
# conRatio: Nyquist ratio percentage
# return: 3D filtered signal array
