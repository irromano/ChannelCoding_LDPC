import numpy as np

a = np.arange(15).reshape(3, 5)  # Creates a 3x5 Matrix of 15 elements, 0-14

print(a)

print(a.shape)  # gives the length of each dim of the Matrix    (3,5)

print(a.ndim)   # gives the dim of the Matrix   2

print(a.dtype.name)  # name of an element's typeobject    int64

print(a.itemsize)  # Size of an element's typeobject    8

print(a.size)   # Number of elements    15

print(type(a))  # Gives datatype of the matrix  <class 'numpy.ndarray'>

b = np.array([6, 7, 8])

print(b)  # [6 7 8]

print(type(b))  # <class 'numpy.ndarray'>
