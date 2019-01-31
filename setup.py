from setuptools import setup

setup(name='sonarNetCDFconverter',
      version='1.0',
      description='This package provides functionality for downloading, reading and writing xml-formats defined by NMD in PYTHON.',
      url='https://github.com/sindrevatnehol/sonarNetCDFconverter/',
      author='Sindre Vatnehol',
      author_email='sindre.vatnehol@hi.no',
      license='GPL3',
      packages=['sonarNetCDFconverter',],
      install_requires=['numpy','lxml','netCDF4','pytz', 'pynmea2', 'datetime',],
      zip_safe=False)

