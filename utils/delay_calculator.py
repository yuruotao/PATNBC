import logging

def calculateDelay(sampling_frequency, reception_delay):
    logging.info('  Function    "calculateDelay"    : %s', __name__)

    delay_offset_samples = 45.8e-6 * sampling_frequency
    active_delay = reception_delay - delay_offset_samples

    return active_delay

# Calculates delay until signal acquisition starts.
# sampling_frequency: Sampling frequency of DAQ
# reception_delay: Time delay until reception of signals
# return: Active delay until acquisition
# why 45.8e-6?