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

array3 = np.array([10, 20, 30, 40, 50])

print(f'array1 * array3 is: {array1 * array3}')


print(f'array3: \nmean:{np.mean(array3)} \nmedian: {np.median(array3)} \nstandard deviation: {np.std(array3)}')

greater_then_25 = array3 > 25

matrix1 = np.array([[1,2,3],[6,4,5]])
# not sure what to do here, because reshaped_array was not possible. i decieded to use data from array1 to make a reshaped_array
reshaped_array = np.array([[1, 2], [4, 5]])
matrix2 = np.dot(reshaped_array, matrix1)

array4 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

array4_mean,array4_median,array4_std = np.mean(array4),np.median(array4),np.std(array4)

print(f'array4 greater then the average of {array4_mean}\n: {array4[array4 > array4_mean]}')