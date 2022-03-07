pyoat
=======================================================

Python Package for Optoacoustic Tomography (OAT)

Installation
-------------------------------------------------------
This project uses pip package manager. Please run the following command in your terminal to install the package.
```bash
pip install git+https://github.com/berkanlafci/pyoat.git
```

Usage
-------------------------------------------------------
After installing package, the functions can be called using python scripts.

Example scripts to use pyoat package can be found in _examples folder.

For example, backprojection reconstruction example on cpu is called with following commands in terminal.
```bash
python exampleCpuBP.py
```
The example scripts can be written by users.

pyoat package can be imported in python scripts using following line.
```python
import pyoat as pt
```
After importing the package, the functions can be called with following lines in python script.
```python
oaData      = pt.oaReader(filePath=filePath) 	# read data
bp          = pt.cpuBP()                      	# create reconstruction object
imageRecon  = bp.recon(oaData.sigMat)         	# reconstruct image
```

Data
-------------------------------------------------------
Test data will be made publicly available.

After the download, place the data in "data/rawData/" folder that shares the same root directory with "exampleCpuBP.py" script that can be run for testing "pyoat".

Citation
-------------------------------------------------------
If you use this package in your research, please cite it as follows

Lafci, B., Ozbek, A., Ozdemir, F., Klimovskaia, A., Perez-Cruz, F., Dean-Ben, X.L., & Razansky, D. (2022). pyoat (Version 1.0.0) [Computer software].

Acknowledgements
-------------------------------------------------------
This project is supported by Swiss Data Science Center (SDSC) grant C19-04.

License
-------------------------------------------------------
This project is licensed under [MIT License](https://mit-license.org/).
