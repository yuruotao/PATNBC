# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#from PySide2.QtCore import *
#from PySide2.QtGui import *
#from PySide2.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from patnbc.user_interface.mpl_widget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1080, 910)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Plot_Visual = MplWidget(self.centralwidget)
        self.Plot_Visual.setObjectName(u"graphicsView")
        self.Plot_Visual.setGeometry(QRect(520, 30, 511, 491))
        font = QFont()
        font.setFamily(u"Times New Roman")
        self.Plot_Visual.setFont(font)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 50, 420, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(10)
        self.pushButton.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(10)
        self.pushButton_2.setFont(font2)


        self.horizontalLayout.addWidget(self.pushButton_2)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 240, 461, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit_6, 5, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit_3, 2, 1, 1, 1)

        self.plainTextEdit_8 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit_8, 7, 1, 1, 1)

        self.plainTextEdit_5 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit_5, 4, 1, 1, 1)

        self.plainTextEdit_4 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit_4, 3, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)

        self.plainTextEdit_7 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setFont(font1)

        self.gridLayout.addWidget(self.plainTextEdit_7, 6, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(50, 150, 441, 71))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(11)
        self.label_2.setFont(font2)

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 0, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 250, 31))
        self.label_3.setFont(font1)
        self.label_3.setScaledContents(True)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(860, 600, 171, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        #self.progressBar = QProgressBar(self.centralwidget)
        #self.progressBar.setObjectName(u"progressBar")
        #self.progressBar.setGeometry(QRect(520, 540, 371, 31))
        #self.progressBar.setFont(font1)
        #self.progressBar.setValue()

        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setFont(font1)
        self.gridLayoutWidget_4.setGeometry(QRect(40, 730, 381, 71))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_4.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_4.addWidget(self.pushButton_5, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.Plot_Visual.raise_()
        self.horizontalLayoutWidget.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_2.raise_()
        # self.progressBar.raise_()
        self.gridLayoutWidget_4.raise_()
        self.label_3.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1301, 17))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Raw Data File", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Transducer Distribution", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Reconstruction Type", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pixel Number", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Low Cutoff Frequency", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Speed of Sound", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Wave Lengths", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Field of View", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Delay Number", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"High Cutoff Frequency", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Backprojection", None))
        self.radioButton_2.setText("")
        self.radioButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Model-based Forward Imaging (in progress)                                           ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Reconstruction Method", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save as .mat", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save as .png", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

