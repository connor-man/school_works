import pandas as pd

info = {
    'Name': ['Mack','George','Francis','Rebbeca','Alex'],
    'Age': [20,32,50,42,11],
    'City':['Buenos Aires','Vienna','Minsk','Santiago','London']

}

dfl = pd.DataFrame(info)

# print('first three people')
# print(dfl.head(3))
# print('')

# print('datatypes in dfl:')
# print(dfl.dtypes)
# print('')

# print('Ages in dfl')
# print(dfl['Age'])
# print('')

# print('Ages greater then 25')
# age_filt = dfl['Age'] > 25
# print(dfl[age_filt])

print('adds saleirs')
salaries =  [2200,336,100_000,1_000_000,4]
dfl.loc[:,'Salary'] = salaries
print(dfl)
print()

# making a copy so that part3's stuff doesnt look wierd
df2 = dfl.copy()
df2.loc[0,'Age'] = pd.NA
df2.loc[3,'Salary'] = pd.NA
df2.fillna(0,inplace=True)
print(df2)
print('')

print('stats description')
print(dfl.describe())
print('')
print('mean age by city')
cities = dfl.groupby(['City'])
print(cities['Age'].mean())
print('')
print('mean salary by city')
print(cities['Salary'].mean())