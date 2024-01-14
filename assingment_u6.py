import numpy as np 
import pandas as pd

array1 = np.arange(1, 11)
array2 = array1 * array1

sliced_array = array1[3:8]
# personal note, the fact that you can do this with slicing both amazes and confunds me
reversed_array = sliced_array[::-1]

matrix1 = np.array(
    [[1,2,3],
     [9,8,7]]
)
transposed_matrix = matrix1.reshape(3,2)

df = pd.read_csv('goobers.csv')

x = df['Fumbles'] + df['Norbid']

df.loc[:,'New_Column'] = x

print(df.describe())

low_norbid = df['Norbid'] < 50

filtered_df = df[low_norbid]
print(filtered_df)