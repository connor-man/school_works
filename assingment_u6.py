import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

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

dorble_type = df['Dorble_type'].value_counts()

plt.figure()
plt.pie(dorble_type, labels=dorble_type.index,autopct='%1.1f%%')
plt.title('The Proportion of Dorble Types of The Goobers')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

plt.figure()
fumble = df['Fumbles']
plt.hist(fumble)
plt.title('Distrubtion of Fumbles Amoung Goobers')
plt.xlabel('Amount')
plt.ylabel('Fumbles')
plt.show()