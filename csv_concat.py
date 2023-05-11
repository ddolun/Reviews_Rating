import pandas as pd
from glob import glob

files = glob('data*.csv')
print(files)
df = pd.concat((pd.read_csv(file, usecols=['Reviews','ckipnlp','score','modelscore'] ) for file in files), ignore_index=True)
print(df.shape)
for index, row in df.iterrows():
    if row['Reviews'] == 'Reviews' :
        df =df.drop([index])
df.to_csv('test2.csv',index = False)
print(df.shape)

# df = pd.read_csv('data63.csv')
# print(df.isnull().sum())