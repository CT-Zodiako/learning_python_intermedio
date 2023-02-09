#python package manager

#PIP https://pypi.org/

import numpy

print(numpy.version.version)

numpy_array = numpy.array([1,42,2,123,1])

print(type(numpy_array))

print(numpy_array*2)


import pandas #pip install pandas

#pip list

#pip uninstall pandas


import requests

#package Aritmetics
from mypackage import arithmetics

print(arithmetics.sum(1,4))