import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

random_array = np.random.randint(1, 150, 20)
random_df = pd.DataFrame({'Values': random_array})
random_df.loc[:,'Squared'] = random_df['Values']*random_df['Values']

plt.figure()
squares = random_df['Squared']
plt.hist(squares)
plt.title('Distrubtion of Values in Squared')
plt.xlabel('Amount')
plt.ylabel('Fumbles')
plt.show()
