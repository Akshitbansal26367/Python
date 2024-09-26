# The power() function is used to raise the elements of an array to a specified power.

"""numpy.diff(arr) function is used when we calculate the n-th order discrete difference along
the given axis. The first order difference is given by out[i] = arr[i+1] – arr[i] along the given axis."""

# The numpy.cross() method computes the cross product of two vectors.

# numpy.sort() function returns a sorted copy of an array.

import numpy as np

input_numbers = np.array([10, 20, 30, 40])

# Raise each number in the array to a fixed power (3)
cubed_numbers = np.power(input_numbers, [3])
print("Cubed numbers array   :", cubed_numbers)

# Raise each number in the array to a varying power
powered_numbers = np.power(input_numbers, [3, 1, 2, 1])
print("Powered numbers array :", powered_numbers)

value_difference = np.diff(input_numbers)
print("Difference array is   :", value_difference)

"""vector1 = np.array([10, 20, 30])
vector2 = np.array([5, 6, 7])
print("Cross Product is      :", np.cross(vector1, vector2))"""

unsorted_arr = np.array([1, 6, 2, 6, 67, 4, 88, 9, 65])
sorted_arr = np.sort(unsorted_arr)
print("Sorted array is       :", sorted_arr)
