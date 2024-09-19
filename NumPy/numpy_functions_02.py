import numpy as np

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

array_2d = np.array([list_a, list_b])

"""flatten() function returns a copy of the array collapsed in one dimension
C means to flatten in row-major order and F means to flatten in column-major order.
Default is C"""

flatten_array_c = array_2d.flatten('C')
flatten_array_f = array_2d.flatten('F')
print("Flatten C :", flatten_array_c)
print("Flatten F :", flatten_array_f)

"""sum() function returns the sum of array elements over the specified axis.
axis : The axis along which we want to calculate the sum value.
axis = 0 means along the column and axis = 1 means working along the row."""

print()
total_sum = np.sum(array_2d)
rows_sums = np.sum(array_2d, axis=1)
column_sums = np.sum(array_2d, axis=0)
print("Sum of all array elements is (row and column) : ", total_sum)
print("Sum of all array elements along the row is    : ", rows_sums)
print("Sum of all array elements along the column is : ", column_sums)

"""nansum() function is used when we want to compute the sum of array elements over a given axis
treating Not a Numbers (NaNs) as zero"""

print()
array_with_nan = np.array([list_a, [5, 6, 7, np.nan]], dtype=float)

rows_sums_with_nan = np.nansum(array_with_nan, axis=1, dtype=int)
column_sums_with_nan = np.nansum(array_with_nan, axis=0, dtype=int)
print("Sum of all array elements along the row is    : ", rows_sums_with_nan)
print("Sum of all array elements along the column is : ", column_sums_with_nan)

"""cumprod() function is used when we want to compute the cumulative product
of array elements over a given axis"""

print()
array_for_cumprod = np.array(list_b)
cumulative_product = np.cumprod(array_for_cumprod)
prod = np.cumprod(array_2d, axis=1)
# print("Cumulative product is", prod)
# print()
print("Cumulative product is", cumulative_product)

"""cumsum() function is used when we want to compute the cumulative sum of array elements
over a given axis."""

print()

# cumulative_sum_along_rows = np.cumsum(array_2d, axis=1)
# print("Cumulative sum is ", cumulative_sum_along_rows)

# print()
cumulative_sum_of_list_a = np.cumsum(list_a)
print("Cumulative sum is ", cumulative_sum_of_list_a)
