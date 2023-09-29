# Gender Identification by Voice

### Python Packages
py -m pip install PACKAGE_NAME
1. SpeechRecognition
2. Pillow
3. pipwin *(Only for Windows users)*
4. sklearn
5. matplotlib
6. pandas

py -m pipwin install PACKAGE_NAME *(Only for Windows users, others can simply install it as above)*
1. PyAudio

### R Packages
1. warbleR
2. tuneR
3. seewave

## Steps to execute
1. Install Python
2. Install R
2. Install required packages for Python and R
3. Run main.py

***Note**: Update the **Rscript** file path in the analyser.py file (if it's different than yours)*

### Download R
1. https://cran.r-project.org/bin/windows/base/

### R Package Installation
1. Open R console and execute **install.packages("PACKAGE_NAME")** and **library("PACKAGE_NAME")** this command.

*If you get any package missing error even after installation of that package then please follow the below steps:*
1. Open R console as an Administrator (close all R console instances first)
2. Execute **.libPaths()** if you get two paths then execute **.libPaths("SECOND_PATH")**
3. Re-install required packages.

***Special thanks to [i-Rohan](https://github.com/i-Rohan/GenderRecognitionByVoice)***
