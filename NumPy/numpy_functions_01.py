import numpy as np

"""
The arange(start,stop, step) : Returns an array with evenly spaced elements as per the interval.

The numpy.zeros() function returns a new array of given shape and type, with zeros. 
Syntax is : numpy.zeros(shape, dtype = None, order = 'C')

The numpy.ones() function returns a new array of given shape and type, with ones.
Syntax is : numpy.ones(shape, dtype = None, order = 'C') 

numpy.full(shape, fill_value, dtype = None, order = ‘C’)
Return a new array with the same shape and type as a given array filled with a fill_value.

The numpy.reshape() function shapes an array without changing the data of the array.
Syntax : numpy.reshape(array, shape, order = 'C')
"""

# Create an array with values starting from 1, incrementing by 0.5, up to but not including 6.2
arr = np.arange(1, 6.2, 0.5)
print("Arrange function use", arr)

# Create an array of zeros with 5 elements of integer type
# zero_arr = np.zeros((2, 5), dtype=int)
zero_arr = np.zeros(5, dtype=int)
print("Zero function use", zero_arr)

# Create an array of ones with 5 elements of integer type
# one_arr = np.ones((2, 5), dtype=int)
one_arr = np.ones(5, dtype=int)
print("Ones function use", one_arr)

# Create an array filled with the value 7, with 5 elements
# full_arr = np.full((2, 5), 7)
full_arr = np.full(5, 7)
print("Full function use", full_arr)

# Create an array from 1 to 10 (inclusive) and reshape it into 2 rows
# The -1 in reshape means "figure out the correct number of columns based on the data"
"""arr = np.arange(1, 11, 1).reshape(2, -1)
print("Reshape function use", arr)"""
