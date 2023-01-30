# PATNBC

Short for Photoacoustic Tomography for Triple Negeative Breast Cancer

## Introduction

Based on the Windows system, PATNBC is implemented within Python 3.8 for medical image forming using the back projection method. We specially designed this for our device of triple-negative breast cancer imaging based on the photoacoustic effect.  
This application underlines the significance of Radon transformation, which is widely used in the area of medical imaging. For instance, MRI and ultrasound imaging.

## Usage

After clicking the software, the welcome interface pops up as shown in Figure 1, a .gif form figure.
![Figure 1](/user_interface/welcome.gif)
After 1.5 seconds of animation, the main window is displayed as shown in Figure 2. We then introduce each module within the main window.
![Figure 2](/readme_files/Fig2.jpg)

By clicking the Raw Data File button on the main window, a window called the Open Matrix File pops up as shown in Figure 3. Selecting the raw data to be processed and hit open, then the raw data is automatically uploaded to the software background.  
![Figure 3](/readme_files/Fig3.png)

If the data format is not compatible with our software, which is .mat, then they wouldn’t be visible to the user by default. Besides, if the process is aborted, a warning window as shown in Figure 4 would appear.  
![Figure 4](/readme_files/Fig4.jpg)

The transducer data we used here specifically target the 3-D transducer distribution, which should also be in the .mat format. The process of data import is similar to the one we described earlier.At the lower bottom of the left-hand side of the main window, there is a default button, after importing the raw data file and transducer distribution file, each of the parameters should be specified. By hitting the Default button, the default parameters are filled within the parameter dialogues.  
PATNBC offers 2 means of reconstruction for selection, Model-based Forward Imaging and Backprojection. Model-based Forward Imaging is still under development. By clicking the circle behind the description, the reconstruction method is selected.  
After clicking the Run button on the lower side of the main window, the program starts to operate. The time span is dependent on the parameters and raw data quantity. The pixel number directly determines the specificity of the reconstructed image. After the reconstruction is finished, the image would be displayed on the image interface on the main window, as shown in Figure 5.  
![Figure 5](/readme_files/Fig5.png)  
To save the displayed image, one can select the output image format, specifically in .mat and .png.

##
