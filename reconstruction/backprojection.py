import time
import h5py
import math
import logging
import numpy as np
import pkg_resources as pkgr
from scipy.sparse.linalg import lsqr
from scipy.sparse import vstack


class backprojection_object():

    # initialization for class backprojection_object
    def __init__(self):
        logging.info('  Class       "backprojection_object"             : %s', __name__)

        self._field_of_view = 0.03
        self._pixel_number = 128
        self._xSensor = {}
        self._ySensor = {}
        self._zSensor = {}
        self._transducer_spatial_distribution = 'ring'
        self._speed_of_sound = 1540
        self._number_of_samples = 2032
        self._sampling_frequency = 40e6
        self._reconstruction_type = 'full'
        self._delay_number_of_samples = 0
        self._wavelengths = [800]
        self.__wavelength_measure_number = 1
        self.__numRepetitions = 1
        self._low_cutoff_frequency = 0.1e6
        self._high_cutoff_frequency = 6e6
        self._butterworth_filter_order = 3

    # field of view
    @property
    def field_of_view(self):
        return self._field_of_view

    @field_of_view.setter
    def field_of_view(self, value):
        logging.info('  Property    "field_of_view"       : %.4f m', value)
        self._field_of_view = value

    @field_of_view.deleter
    def field_of_view(self):
        del self._field_of_view

    # pixel number
    @property
    def pixel_number(self):
        return self._pixel_number

    @pixel_number.setter
    def pixel_number(self, value):
        logging.info('  Property    "pixel_number"       : %d ', value)
        self._pixel_number = value

    @pixel_number.deleter
    def pixel_number(self):
        del self._pixel_number

    # x positions of sensor
    @property
    def xSensor(self):
        return self._xSensor

    @xSensor.setter
    def xSensor(self, value):
        self._xSensor = value

    @xSensor.deleter
    def xSensor(self):
        del self._xSensor

    # y positions of sensor
    @property
    def ySensor(self):
        return self._ySensor

    @ySensor.setter
    def ySensor(self, value):
        self._ySensor = value

    @ySensor.deleter
    def ySensor(self):
        del self._ySensor

    # z positions of sensor
    @property
    def zSensor(self):
        return self._zSensor

    @zSensor.setter
    def zSensor(self, value):
        self._zSensor = value

    @zSensor.deleter
    def zSensor(self):
        del self._zSensor

    # array properties
    @property
    def arrayData(self):
        return self.__arrayData

    @arrayData.setter
    def arrayData(self, value):
        self.__arrayData = value

    @arrayData.deleter
    def arrayData(self):
        del self.__arrayData

    # the spatial distribution of the transducers
    @property
    def transducer_spatial_distribution(self):
        return self._transducer_spatial_distribution

    @transducer_spatial_distribution.setter
    def transducer_spatial_distribution(self, value):
        logging.info('  Property    "transducer_spatial_distribution"           : %s', value)
        self._transducer_spatial_distribution = value
        self.__arrayDir = pkgr.resource_filename('patnbc', 'arrays/' + self._transducer_spatial_distribution + '.mat')
        self.__arrayData = h5py.File(self.__arrayDir, 'r')
        self.xSensor = self.__arrayData['transducerPos'][0, :]
        self.ySensor = self.__arrayData['transducerPos'][1, :]
        self.zSensor = self.__arrayData['transducerPos'][2, :]

    @transducer_spatial_distribution.deleter
    def transducer_spatial_distribution(self):
        del self._transducer_spatial_distribution
        del self.xSensor
        del self.ySensor
        del self.zSensor

    # speed of sound
    @property
    def speed_of_sound(self):
        return self._speed_of_sound

    @speed_of_sound.setter
    def speed_of_sound(self, value):
        logging.info('  Property    "speed_of_sound"      : %d m/s', value)
        self._speed_of_sound = value

    @speed_of_sound.deleter
    def speed_of_sound(self):
        del self._speed_of_sound

    # number of samples
    @property
    def number_of_samples(self):
        return self._number_of_samples

    @number_of_samples.setter
    def number_of_samples(self, value):
        logging.info('  Property    "number_of_samples"          : %d ', value)
        self._number_of_samples = value

    @number_of_samples.deleter
    def number_of_samples(self):
        del self._number_of_samples

    # sampling frequency
    @property
    def sampling_frequency(self):
        return self._sampling_frequency

    @sampling_frequency.setter
    def sampling_frequency(self, value):
        logging.info('  Property    "sampling_frequency"         : %d Hz', value)
        self._sampling_frequency = value

    @sampling_frequency.deleter
    def sampling_frequency(self):
        del self._sampling_frequency

    # reconstruction type
    @property
    def reconstruction_type(self):
        return self._reconstruction_type

    @reconstruction_type.setter
    def reconstruction_type(self, value):
        logging.info('  Property    "reconstruction_type"         : %s ', value)
        self._reconstruction_type = value

    @reconstruction_type.deleter
    def reconstruction_type(self):
        del self._reconstruction_type

    # delay in samples
    @property
    def delay_number_of_samples(self):
        return self._delay_number_of_samples

    @delay_number_of_samples.setter
    def delay_number_of_samples(self, value):
        logging.info('  Property    "delay_number_of_samples"    : %.4f ', value)
        self._delay_number_of_samples = value

    @delay_number_of_samples.deleter
    def delay_number_of_samples(self):
        del self._delay_number_of_samples

    # wavelengths
    @property
    def wavelengths(self):
        return self._wavelengths

    @wavelengths.setter
    def wavelengths(self, value):
        logging.info('  Property    "wavelengths"       : {} nm'.format(', '.join(map(str, value))))
        self._wavelengths = value
        self.wavelength_measure_number = len(value)

    @wavelengths.deleter
    def wavelengths(self):
        del self._wavelengths

    # number of wavelengths
    @property
    def wavelength_measure_number(self):
        return self.__wavelength_measure_number

    @wavelength_measure_number.setter
    def wavelength_measure_number(self, value):
        self.__wavelength_measure_number = value

    @wavelength_measure_number.deleter
    def wavelength_measure_number(self):
        del self.__wavelength_measure_number

    # number of repetitions
    @property
    def numRepetitions(self):
        return self.__numRepetitions

    @numRepetitions.setter
    def numRepetitions(self, value):
        self.__numRepetitions = value

    @numRepetitions.deleter
    def numRepetitions(self):
        del self.__numRepetitions

    # low cutoff frequency of filter
    @property
    def low_cutoff_frequency(self):
        return self._low_cutoff_frequency

    @low_cutoff_frequency.setter
    def low_cutoff_frequency(self, value):
        logging.info('  Property    "low_cutoff_frequency"         : %d Hz', value)
        self._low_cutoff_frequency = value

    @low_cutoff_frequency.deleter
    def low_cutoff_frequency(self):
        del self._low_cutoff_frequency

    # high cutoff frequency of filter
    @property
    def high_cutoff_frequency(self):
        return self._high_cutoff_frequency

    @high_cutoff_frequency.setter
    def high_cutoff_frequency(self, value):
        logging.info('  Property    "high_cutoff_frequency"        : %d Hz', value)
        self._high_cutoff_frequency = value

    @high_cutoff_frequency.deleter
    def high_cutoff_frequency(self):
        del self._high_cutoff_frequency

    # order of filter
    @property
    def butterworth_filter_order(self):
        return self._butterworth_filter_order

    @butterworth_filter_order.setter
    def butterworth_filter_order(self, value):
        logging.info('  Property    "butterworth_filter_order"            : %d ', value)
        self._butterworth_filter_order = value

    @butterworth_filter_order.deleter
    def butterworth_filter_order(self):
        del self._butterworth_filter_order

    # reconstruction function
    def backprojection_reconstruction_function(self, sigMat):
        logging.info('  Function    "backprojection_reconstruction_function"           : %s', __name__)

        from patnbc import sigMatFilter, sig_mat_normalization

        if np.ndim(sigMat) == 2:
            sigMat = np.expand_dims(sigMat, axis=2)

        pixel_number = self.pixel_number
        xSensor = self.xSensor
        ySensor = self.ySensor
        zSensor = self.zSensor
        sampling_frequency = self.sampling_frequency
        self.numRepetitions = int(np.ceil(np.shape(sigMat)[2] / self.wavelength_measure_number))
        self.number_of_samples = np.shape(sigMat)[0]

        # filter sigMat
        sigMatF = (-1) * sigMatFilter(sigMat, self.low_cutoff_frequency, self.high_cutoff_frequency, sampling_frequency,
                                      self.butterworth_filter_order, 0.5)

        # normalize mean of sigMat around 0
        sigMatN = sig_mat_normalization(sigMatF)

        # beginning of reconstruction
        print('***** reconstruction *****')
        startTime = time.time()

        timePoints = np.linspace(0, self.number_of_samples / sampling_frequency, self.number_of_samples) \
                     + self.delay_number_of_samples / sampling_frequency

        # reconstructed image (output of this function)
        reconstructed_image = np.zeros((pixel_number, pixel_number, self.wavelength_measure_number, self.numRepetitions))
        # each picture is pixel_number * pixel_number, there are wavelength_measure_number * numRepetitions of images

        # length of one pixel
        pixel_length = self.field_of_view / (pixel_number - 1)

        # define imaging grid
        x = np.linspace(((-1) * (pixel_number / 2 - 0.5) * pixel_length), ((pixel_number / 2 - 0.5) * pixel_length), pixel_number)
        y = np.linspace(((-1) * (pixel_number / 2 - 0.5) * pixel_length), ((pixel_number / 2 - 0.5) * pixel_length), pixel_number)
        meshX, meshY = np.meshgrid(x, y)

        # loop through repetitions
        for repetition_counter in range(0, self.numRepetitions):

            # loop through wavelengths
            for wavelength_counter in range(0, self.wavelength_measure_number):

                # loop through all transducer elements
                for sensor_counter in range(0, len(xSensor)):

                    # distribute the corresponding signal for transducer element
                    # note the input data format here:
                    # [row, column, [other dimensions summarized number] ], the following is the depiction of one dimension
                    # [     sensor1, sensor2, ...,     sensorN]
                    # [time1                                  ]
                    # [time2                                  ]
                    # [time3                                  ]
                    # [...                                    ]
                    # [timeM                                  ]
                    # [in each repetition, the wavelengths are looped, the total number is repetition number * wavelength number]
                    signal_separated_for_single_transducer = sigMatN[:, sensor_counter, [(repetition_counter * self.wavelength_measure_number) + wavelength_counter]]

                    # calculate derivative of the signal for 'derivative' and 'full' methods
                    diffSignal = np.concatenate((signal_separated_for_single_transducer[1:] - signal_separated_for_single_transducer[0:-1], [[0]]), axis=0)
                    derSignal = np.multiply(diffSignal, np.expand_dims(timePoints, axis=1)) * sampling_frequency

                    # distance of detector to image grid
                    distX = meshX - xSensor[sensor_counter]
                    distY = meshY - ySensor[sensor_counter]
                    dist = np.sqrt(distX ** 2 + distY ** 2)

                    # find corresponding sample value for distance
                    timeSample = np.ceil(
                        (dist * sampling_frequency) / self.speed_of_sound - self.delay_number_of_samples)
                    timeSample = timeSample.astype(int)

                    # apply number of samples bounds
                    timeSample[timeSample <= 0] = 0
                    timeSample[timeSample >= self.number_of_samples - 2] = self.number_of_samples - 3

                    # reconstruct image based on the defined method
                    if self.reconstruction_type == 'direct':
                        reconstructed_image[:, :, wavelength_counter, repetition_counter] = reconstructed_image[:, :, wavelength_counter,
                                                                     repetition_counter] + np.squeeze(
                            signal_separated_for_single_transducer[timeSample])
                    elif self.reconstruction_type == 'derivative':
                        reconstructed_image[:, :, wavelength_counter, repetition_counter] = reconstructed_image[:, :, wavelength_counter,
                                                                     repetition_counter] - np.squeeze(
                            derSignal[timeSample])
                    elif self.reconstruction_type == 'full':
                        reconstructed_image[:, :, wavelength_counter, repetition_counter] = reconstructed_image[:, :, wavelength_counter,
                                                                     repetition_counter] + np.squeeze(
                            signal_separated_for_single_transducer[timeSample] - derSignal[timeSample])
                    else:
                        reconstructed_image[:, :, wavelength_counter, repetition_counter] = reconstructed_image[:, :, wavelength_counter,
                                                                     repetition_counter] + np.squeeze(
                            signal_separated_for_single_transducer[timeSample] - derSignal[timeSample])

        endTime = time.time()
        print('time elapsed: %.2f' % (endTime - startTime))

        # end of reconstruction
        return reconstructed_image


# sigMat: Array that contains signals
# return: 4D reconstructed image (height x width x wavelengths x repetition)


# -----------------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------- model based --------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------#

# recon model based class
class model_based_reconstruction():
    """
 field_of_view: Field of view in x and y direction in meters (default: 0.03)
 nAngles: Number of angles used in model
 pixel_number: Number of pixels in image (default: 128)
 xSensor: X position of transducer elements (default: Ring array positions)
 ySensor: Y position of transducer elements (default: Ring array positions)
 rSensor: Radius of transducer array
 angleSensor: Angles of individual transducer elements
 transducer_spatial_distribution: Array type used in experiment (default: Ring array)
 speed_of_sound: Estimated speed of sound (m/s) based on temperature (default: 1540 m/s)
 number_of_samples: Number of samples in sigMat (default: 2032)
 sampling_frequency: Sampling frequency of signals (default: 40e6)
 delay_number_of_samples: Active delay of signals (default: 61)
 wavelengths: Wavelengths used in illumination (default: 800 nm)
 wavelength_measure_number: Number of wavelengths used in acquisition
 numRepetitions: Number of repetitions
 low_cutoff_frequency: Low cut off frequency of bandpass filter in MHz (default: 0.1e6 MHz)
 high_cutoff_frequency: High cut off frequency of bandpass filter in MHz (default: 6e6 MHz)
 butterworth_filter_order: Butterworth filter order
 numIteration: Number of iterations in minimization function
 regMethod: Regularization method
 return: model_based_reconstruction object
    """

    # initialization for class model_based_reconstruction_object
    def __init__(self):
        logging.info('  Class       "model_based_reconstruction"             : %s', __name__)

        self._field_of_view = 0.03
        self._nAngles = 256
        self._pixel_number = 128
        self._xSensor = {}
        self._ySensor = {}
        self._rSensor = {}
        self._angleSensor = {}
        self._transducer_spatial_distribution = 'ring'
        self._speed_of_sound = 1540
        self._number_of_samples = 2032
        self._sampling_frequency = 40e6
        self._delay_number_of_samples = 0
        self._wavelengths = [800]
        self._wavelength_measure_number = 1
        self._numRepetitions = 1
        self._low_cutoff_frequency = 0.1e6
        self._high_cutoff_frequency = 6e6
        self._butterworth_filter_order = 3
        self._numIterations = 5
        self._regMethod = None
        self._lambdaReg = 15e6

    # --------------------------------#
    # ---------- properties ----------#
    # --------------------------------#

    # field of view
    @property
    def field_of_view(self):
        return self._field_of_view

    @field_of_view.setter
    def field_of_view(self, value):
        logging.info('  Property    "field_of_view"       : %.4f m', value)
        self._field_of_view = value

    @field_of_view.deleter
    def field_of_view(self):
        del self._field_of_view

    # number of angles
    @property
    def nAngles(self):
        return self._nAngles

    @nAngles.setter
    def nAngles(self, value):
        self._nAngles = value

    @nAngles.deleter
    def nAngles(self):
        del self._nAngles

    # pixel number
    @property
    def pixel_number(self):
        return self._pixel_number

    @pixel_number.setter
    def pixel_number(self, value):
        logging.info('  Property    "pixel_number"       : %d ', value)
        self._pixel_number = value
        self._nAngles = 2 * value

    @pixel_number.deleter
    def pixel_number(self):
        del self._pixel_number

    # x positions of sensor
    @property
    def xSensor(self):
        return self._xSensor

    @xSensor.setter
    def xSensor(self, value):
        self._xSensor = value

    @xSensor.deleter
    def xSensor(self):
        del self._xSensor

    # y positions of sensor
    @property
    def ySensor(self):
        return self._ySensor

    @ySensor.setter
    def ySensor(self, value):
        self._ySensor = value

    @ySensor.deleter
    def ySensor(self):
        del self._ySensor

    # --------------------------------#
    # radius of sensor

    @property
    def rSensor(self):
        return self._rSensor

    @rSensor.setter
    def rSensor(self, value):
        self._rSensor = value

    @rSensor.deleter
    def rSensor(self):
        del self._rSensor

    # sensor angle
    @property
    def angleSensor(self):
        return self._angleSensor

    @angleSensor.setter
    def angleSensor(self, value):
        self._angleSensor = value

    @angleSensor.deleter
    def angleSensor(self):
        del self._angleSensor

    # cup type
    @property
    def transducer_spatial_distribution(self):
        return self._transducer_spatial_distribution

    @transducer_spatial_distribution.setter
    def transducer_spatial_distribution(self, value):
        logging.info('  Property    "transducer_spatial_distribution"           : %s', value)
        self._transducer_spatial_distribution = value
        self.__arrayDir = pkgr.resource_filename('patnbc', 'arrays/' + self._transducer_spatial_distribution + '.mat')
        self.__arrayData = h5py.File(self.__arrayDir, 'r')
        self.xSensor = self.__arrayData['transducerPos'][0, :]
        self.ySensor = self.__arrayData['transducerPos'][1, :]
        self.rSensor = np.sqrt(self.xSensor ** 2 + self.ySensor ** 2)
        self.angleSensor = np.arctan2(self.ySensor, self.xSensor) + 2 * math.pi * (
            np.multiply((self.xSensor > 0), (self.ySensor < 0)))

    @transducer_spatial_distribution.deleter
    def transducer_spatial_distribution(self):
        del self._transducer_spatial_distribution
        del self.xSensor
        del self.ySensor
        del self.rSensor

    # speed of sound
    @property
    def speed_of_sound(self):
        return self._speed_of_sound

    @speed_of_sound.setter
    def speed_of_sound(self, value):
        logging.info('  Property    "speed_of_sound"      : %d m/s', value)
        self._speed_of_sound = value

    @speed_of_sound.deleter
    def speed_of_sound(self):
        del self._speed_of_sound

    # number of samples
    @property
    def number_of_samples(self):
        return self._number_of_samples

    @number_of_samples.setter
    def number_of_samples(self, value):
        logging.info('  Property    "number_of_samples"          : %d ', value)
        self._number_of_samples = value

    @number_of_samples.deleter
    def number_of_samples(self):
        del self._number_of_samples

    # sampling frequency
    @property
    def sampling_frequency(self):
        return self._sampling_frequency

    @sampling_frequency.setter
    def sampling_frequency(self, value):
        logging.info('  Property    "sampling_frequency"         : %d Hz', value)
        self._sampling_frequency = value

    @sampling_frequency.deleter
    def sampling_frequency(self):
        del self._sampling_frequency

    # delay in samples
    @property
    def delay_number_of_samples(self):
        return self._delay_number_of_samples

    @delay_number_of_samples.setter
    def delay_number_of_samples(self, value):
        logging.info('  Property    "delay_number_of_samples"    : %.4f ', value)
        self._delay_number_of_samples = value

    @delay_number_of_samples.deleter
    def delay_number_of_samples(self):
        del self._delay_number_of_samples

    # wavelengths
    @property
    def wavelengths(self):
        return self._wavelengths

    @wavelengths.setter
    def wavelengths(self, value):
        logging.info('  Property    "wavelengths"       : {} nm'.format(', '.join(map(str, value))))
        self._wavelengths = value
        self.wavelength_measure_number = len(value)

    @wavelengths.deleter
    def wavelengths(self):
        del self._wavelengths

    # number of wavelengths
    @property
    def wavelength_measure_number(self):
        return self._wavelength_measure_number

    @wavelength_measure_number.setter
    def wavelength_measure_number(self, value):
        self._wavelength_measure_number = value

    @wavelength_measure_number.deleter
    def wavelength_measure_number(self):
        del self._wavelength_measure_number

    # number of repetitions
    @property
    def numRepetitions(self):
        return self._numRepetitions

    @numRepetitions.setter
    def numRepetitions(self, value):
        self._numRepetitions = value

    @numRepetitions.deleter
    def numRepetitions(self):
        del self._numRepetitions

    # low cutoff frequency of filter
    @property
    def low_cutoff_frequency(self):
        return self._low_cutoff_frequency

    @low_cutoff_frequency.setter
    def low_cutoff_frequency(self, value):
        logging.info('  Property    "low_cutoff_frequency"         : %d Hz', value)
        self._low_cutoff_frequency = value

    @low_cutoff_frequency.deleter
    def low_cutoff_frequency(self):
        del self._low_cutoff_frequency

    # high cutoff frequency of filter
    @property
    def high_cutoff_frequency(self):
        return self._high_cutoff_frequency

    @high_cutoff_frequency.setter
    def high_cutoff_frequency(self, value):
        logging.info('  Property    "high_cutoff_frequency"        : %d Hz', value)
        self._high_cutoff_frequency = value

    @high_cutoff_frequency.deleter
    def high_cutoff_frequency(self):
        del self._high_cutoff_frequency

    # order of filter
    @property
    def butterworth_filter_order(self):
        return self._butterworth_filter_order

    @butterworth_filter_order.setter
    def butterworth_filter_order(self, value):
        logging.info('  Property    "butterworth_filter_order"            : %d ', value)
        self._butterworth_filter_order = value

    @butterworth_filter_order.deleter
    def butterworth_filter_order(self):
        del self._butterworth_filter_order

    # iteration number
    @property
    def numIterations(self):
        return self._numIterations

    @numIterations.setter
    def numIterations(self, value):
        logging.info('  Property    "numIterations"     : %d ', value)
        self._numIterations = value

    @numIterations.deleter
    def numIterations(self):
        del self._numIterations

    # regularization method
    @property
    def regMethod(self):
        return self._regMethod

    @regMethod.setter
    def regMethod(self, value):
        logging.info('  Property    "regMethod"         : %s ', value)
        self._regMethod = value

    @regMethod.deleter
    def regMethod(self):
        del self._regMethod

    # regularization method
    @property
    def lambdaReg(self):
        return self._lambdaReg

    @lambdaReg.setter
    def lambdaReg(self, value):
        logging.info('  Property    "lambdaReg"         : %s ', value)
        self._lambdaReg = value

    @lambdaReg.deleter
    def lambdaReg(self):
        del self._lambdaReg

    # model matrix calculation
    def calculateModelMatrix(self):
        logging.info('  Function    "calculateModelMatrix"  : %s', __name__)

        from patnbc import forward_model_photoacoustic_object

        print('***********************************')
        print('*** Calculating model matrix... ***')

        # initialize photoacoustic model
        mOA = forward_model_photoacoustic_object()

        # set OA model parameters
        mOA.field_of_view = self.field_of_view
        mOA.pixel_number = self.pixel_number
        mOA.speed_of_sound = self.speed_of_sound
        mOA.number_of_samples = self.number_of_samples
        mOA.sampling_frequency = self.sampling_frequency
        mOA.regMethod = self.regMethod
        mOA.rSensor = self.rSensor
        mOA.angleSensor = self.angleSensor
        mOA.nAngles = self.nAngles
        mOA.delay_number_of_samples = self.delay_number_of_samples

        timePoints = np.linspace(0, (self.number_of_samples - 2) / self.sampling_frequency,
                                 self.number_of_samples - 2) + self.delay_number_of_samples / self.sampling_frequency

        modelMatrix = mOA.calculateModel(timePoints)

        return modelMatrix

    # recon matrix calculation

    def calculateReconMatrix(self, modelMatrix):
        logging.info('  Function    "calculateReconMatrix"  : %s', __name__)
        from patnbc import forward_model_photoacoustic_object
        print('***** Merging matrices *****')

        # initialize photoacoustic model
        mOA = forward_model_photoacoustic_object()

        # set regularization parameters
        mOA.pixel_number = self.pixel_number
        mOA.lambdaReg = self.lambdaReg

        if self.regMethod == 'tikonov':
            regMatrix = mOA.calculateRegularizationMatrix()
            reconMatrix = vstack((modelMatrix, regMatrix))
        else:
            reconMatrix = modelMatrix

        return reconMatrix

    # Merge model matrix and regularization matrix
    # return: Recon matrix which is combination of model matrix and regularization matrix

    # reconstruction function

    def recon(self, sigMat, reconMatrix):
        """
        Model based reconstruction function on CPU for photoacoustic imaging

        :param sigMat:          Array that contains signals
        :param reconMatrix:     Combined model matrix and regularization matrix

        :return: 4D reconstructed image (height x width x wavelengths x repetition)
        """
        logging.info('  Function    "recon"             : %s', __name__)

        from patnbc import sigMatFilter, sig_mat_normalization

        if np.ndim(sigMat) == 2:
            sigMat = np.expand_dims(sigMat, axis=2)

        pixel_number = self.pixel_number
        self.numRepetitions = int(np.ceil(np.shape(sigMat)[2] / self.wavelength_measure_number))

        # filter sigMat
        sigMatF = (-1) * sigMatFilter(sigMat, self.low_cutoff_frequency, self.high_cutoff_frequency,
                                      self.sampling_frequency, self.butterworth_filter_order, 0.5)

        # normalize mean of sigMat around 0
        sigMatN = sig_mat_normalization(sigMatF)

        # reconstructed image (output of this function)
        reconstructed_image = np.zeros((pixel_number, pixel_number, self.wavelength_measure_number, self.numRepetitions))

        # beginning of reconstruction
        print('***** reconstruction *****')
        startTime = time.time()

        # loop through repetitions
        for repetition_counter in range(0, self.numRepetitions):

            # loop through wavelengths
            for wavelength_counter in range(0, self.wavelength_measure_number):

                sigMatVec = np.expand_dims(
                    np.transpose(sigMatN[:, :, [(repetition_counter * self.wavelength_measure_number) + wavelength_counter]]).reshape(-1), axis=1)

                if self.regMethod == 'tikonov':
                    bVec = np.concatenate((sigMatVec, np.zeros((pixel_number * pixel_number, 1))))
                else:
                    bVec = sigMatVec

                recon, reasonTerm, iterNum, normR = lsqr(reconMatrix, bVec, iter_lim=self.numIterations)[:4]
                reconstructed_image[:, :, wavelength_counter, repetition_counter] = np.reshape(recon, (pixel_number, pixel_number))

        endTime = time.time()
        print('time elapsed: %.2f' % (endTime - startTime))

        # end of reconstruction
        return reconstructed_image

# Back projection reconstruction class for photoacoustic imaging
# field_of_view: Field of view in x and y direction in meters (default: 0.03)
# pixel_number: Number of pixels in image (default: 128)
# xSensor: X position of transducer elements (default: Ring array positions)
# ySensor: Y position of transducer elements (default: Ring array positions)
# transducer_spatial_distribution: Array type used in experiment (default: Ring array)
# speed_of_sound: Estimated speed of sound (m/s) based on temperature (default: 1540 m/s)
# number_of_samples: Number of samples in sigMat (default: 2032)
# sampling_frequency: Sampling frequency of signals (default: 40e6)
# reconstruction_type: Reconstruction type for backprojection (default: full)
# delay_number_of_samples: Active delay of signals (default: 61)
# wavelengths: Wavelengths used in illumination (default: 800 nm)
# wavelength_measure_number: Number of wavelengths used in acquisition
# numRepetitions: Number of repetitions
# high_cutoff_frequency: High cut off frequency of bandpass filter in MHz (default: 6e6 MHz)
# butterworth_filter_order: Butterworth filter order
# return: backprojection_object object
