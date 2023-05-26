import pandas as pd
from glob import glob

# 合併檔案
files = glob(r'D:\vscode\python\reviews_rating\CSV\訓練集\data41*.csv')
print(files)
df = pd.concat((pd.read_csv(file, usecols=['Reviews','ckipnlp','score','modelscore'] ) for file in files), ignore_index=True)
print(df.shape)
for index, row in df.iterrows():
    if row['Reviews'] == 'Reviews' :
        df =df.drop([index])
df.to_csv('',index = False)
print(df.shape)
print(df.isnull().sum())

# 檢查空值
# df = pd.read_csv('R2testdata.csv')
# print(df.isnull().sum())

# 刪除無用欄位
# df = pd.read_csv('SVMv2.csv', usecols=['Name','Reviews','ckipnlp','score','modelscore','sub_score'])
# df.to_csv('SVMversion2.csv' , index=False)