import numpy as np

"""
NumPy is a Python Package which stands for Numerical Python.
It is the core library for scientific computation which contains
a powerful n-dimensional array object
"""

"""
NumPy array : It is a powerful N-dimensional array object which is in the form of
rows and columns
"""

a = np.array([2, 3, 4, 0, 1, 7])
print("1-D array is      ", a)
print("1-D array type is ", type(a))
print("1-D Array slicing", a[0:2])

# print()
# b = np.array([(1, 2, 3), (4, 5, 6)])
# print("2-D array is", b)

"""
We can slice instead of index like this : [start:end]
We can also define the step, like this : [start:end:step]
If we don't pass start index is considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step is considered 1
"""

# Create two lists with six elements each
l1 = [10, 20, 30, 50, 90, 15]
l2 = [11, 21, 31, 51, 91, 16]

# Create a 2-dimensional NumPy array 'ar' by combining the two lists
ar = np.array([l1, l2])
print()

# Perform array slicing to extract elements at column index 1 from both rows
# print("2-D Array slicing", ar[0:2, 1])
# print("2-D Array slicing", ar[0:2, 0:2])

"""
ndarray.ndim : number of axes (dimensions) of the array.

ndarray.shape : the dimensions of the array. This is a tuple of integers indicating 
the size of the array in each dimension. For a matrix with n rows and m columns,
shape will be (n, m). The length of the shape tuple is therefore the number of axes, ndim.

ndarray.size : the total number of elements of the array. This is equal to the product of 
the elements of shape

ndarray.dtype : an object describing the type of the elements in the array. One can 
create or specify dtype's using Standard Python types. Additionally NumPy provides types of its own.  
"""

c = np.array([[10, 20, 30, 40, 50], [22, 55, 66, 77, 88]])
print("ndim   : ", c.ndim)
print("shape  : ", c.shape)
print("size   : ", c.size)
print("dtype  : ", c.dtype)
