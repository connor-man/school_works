# imports numpy and gives it the alias np, which is shorter and easier to work with
import numpy as np

# creates a 1d array of intergers
array1 = np.array([1, 2, 3, 4, 5])
# creates a 2d array of intergers
array2 = np.array([[1, 2, 3], [4, 5, 6]])
# prints certain attributes about the arrays
print(f'array 1 features:\nshape: {array1.shape}\nsize: {array1.size}\ndata type: {array1.dtype}\n')
print(f'array 2 features:\nshape: {array2.shape}\nsize: {array2.size}\ndata type: {array2.dtype}')

try:
    reshaped_array = array1.reshape(2, 2)
    print('array succsuflly resized')
except:
    print('could not be resized')
print()
print(f'the second item in array1 is: {array1[1]}')

print(f'the item at row 2, column 3 of array2 is: {array2[1,2]}')
