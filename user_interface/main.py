import sys
import cgitb
#from PySide2.QtWidgets import QApplication, QMainWindow
#from PySide2.QtCore import QFile
from patnbc.user_interface.ui_main_window import Ui_MainWindow
from patnbc.user_interface.welcome_animation import *
from patnbc.data_reader import *
from patnbc import *
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QMainWindow
from PyQt5.Qt import qApp, QTimer
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool,pyqtSignal)
import re
from os.path import basename, dirname
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent=parent)
        qApp.installEventFilter(self)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.load_raw_data_file)
        self.pushButton_2.clicked.connect(self.load_transducer_array_type)
        self.pushButton_6.clicked.connect(self.parameter_default)
        self.pushButton_5.clicked.connect(self.run_main)
        # push_button_4: save as mat
        self.pushButton_4.clicked.connect(self.save_mat)
        self.pushButton_3.clicked.connect(self.save_png)


# load the raw data file
    def load_raw_data_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folderPath, _ = QFileDialog.getOpenFileName(self, "Open Matrix File", "",
                                                  "Matrix File (*.mat)")
        if folderPath:
            global folderPath_1
            folderPath_1 = folderPath.rstrip("raw_data")
            filename = str(basename(folderPath))
            filename = filename.rstrip(".mat")
            folderPath = str(folderPath)
            folderPath = folderPath.rstrip("/" + filename + ".mat")
            global sigMat
            raw_data = photoacoustic_data_reader(folderPath=folderPath, scanName=filename, averaging=False)
            sigMat = raw_data.sigMat
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('No file is loaded')
            msg.setInformativeText("Please select a file")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            pass

    def load_transducer_array_type(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folderPath, _ = QFileDialog.getOpenFileName(self, "Open Matrix File", "",
                                                    "Matrix File (*.mat)")
        if folderPath:
           filename = str(basename(folderPath))
           filename = filename.rstrip(".mat")
           global transducer_spatial_distribution
           transducer_spatial_distribution = filename
           self.plainTextEdit_4.setPlainText(filename)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('No file is loaded')
            msg.setInformativeText("Please select a file")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            pass


    def parameter_default(self):
        self.plainTextEdit.setPlainText("1535")
        self.plainTextEdit_2.setPlainText("0.024")
        self.plainTextEdit_3.setPlainText("512")
        self.plainTextEdit_4.setPlainText("ring")
        self.plainTextEdit_5.setPlainText("64")
        self.plainTextEdit_6.setPlainText("800")
        self.plainTextEdit_7.setPlainText("0.1")
        self.plainTextEdit_8.setPlainText("6")

    def visualization(self, d2image):
        self.Plot_Visual.canvas.ax.clear()
        self.Plot_Visual.canvas.draw()

        self.Plot_Visual.canvas.ax.imshow(d2image[:, :, 0, 0])
        self.Plot_Visual.canvas.fig.tight_layout()
        self.Plot_Visual.canvas.draw()
        global reconstructed_imageRotated
        reconstructed_imageRotated = np.rot90(d2image, 1)


    def run_main(self):
        speed_of_sound = float(self.plainTextEdit.toPlainText())
        field_of_view = float(self.plainTextEdit_2.toPlainText())
        pixel_number = float(self.plainTextEdit_3.toPlainText())
        transducer_spatial_distribution = self.plainTextEdit_4.toPlainText()
        delay_number_of_samples = float(self.plainTextEdit_5.toPlainText())
        wavelengths = self.plainTextEdit_6.toPlainText().split(",")
        for i in range(len(wavelengths)):
            wavelengths[i] = float(wavelengths[i])
        low_cutoff_frequency = float(self.plainTextEdit_7.toPlainText())
        high_cutoff_frequency = float(self.plainTextEdit_8.toPlainText())


        global bp
        bp = backprojection_object()
        bp.speed_of_sound = speed_of_sound  # change SoS based on water temperature (default: 1480)
        bp.field_of_view = field_of_view  # FOV to reconstruct (default: 0.03)
        bp.pixel_number = pixel_number  # increase this number for higher resolution (default: 128)
        bp.transducer_spatial_distribution = transducer_spatial_distribution  # ring, multisegment, virtualRing (default: ringCup)
        bp.reconstruction_type = 'full'  # full, direct or derivative (default: full)
        bp.delay_number_of_samples = delay_number_of_samples  # reception delay in samples
        bp.wavelengths = wavelengths  # wavelengths used in acquisition
        bp.low_cutoff_frequency = low_cutoff_frequency  # low cutoff for bandpass (default: 0.1e6)
        bp.high_cutoff_frequency = high_cutoff_frequency  # high cutoff for bandpass (default: 6e6)
        reconstructed_image = bp.backprojection_reconstruction_function(sigMat)


    def save_mat(self):
        pngPath = folderPath_1 + 'result\\figure'
        saveImagePng(reconObject=bp, pngPath=pngPath, saveName='BackProjection_fig',
                     reconstructed_image=reconstructed_imageRotated)

    def save_png(self):
        pngPath = folderPath_1 + 'result\\figure'
        saveImagePng(reconObject=bp, pngPath=pngPath, saveName='BackProjection_fig',
                     reconstructed_image=reconstructed_imageRotated)

if __name__ == "__main__":
    cgitb.enable(format='text')
    app = QApplication(sys.argv)
    main_window = Main_Window()
    folderPath_root = str(Path.cwd())

    # the color template can be altered using the following code
    #with open(folderPath_root + '/qss/template.qss', "r") as qss_file:
    #    _style = qss_file.read()
    #    app.setStyleSheet(_style)

# animation introduction
    global splash
    splash = GifSplashScreen()
    splash.show()
    splash.duration(app, 1.5)
    splash.close()

# display the main window
    main_window.show()

    sys.exit(app.exec_())
