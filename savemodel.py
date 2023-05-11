from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
import numpy as np
from sklearn.svm import SVR
import pandas as pd
import pickle

sentences = []
scores = []
rows = pd.read_csv('1234.csv')
i = 0 
for index, row in rows.iterrows():
    sentences.append(row['ckipnlp'])
    scores.append(row['score'])
    i+=1
print("評分了{}筆評論".format(i))

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vector = pickle.load(f)

# 將中文句子轉換為詞向量
X = vector.transform(sentences)
y = np.array(scores)


# # 確保特徵向量的維度和類型與訓練時相同
# if X.shape[1] != model.support_vectors_.shape[1]:
#     raise ValueError("Feature vector dimension mismatch.")
# if not isinstance(X, type(model.support_vectors_)):
#     raise TypeError("Feature vector type mismatch.")

pred=model.predict(X)
for index,row in rows.iterrows():
    sub_score = row['score'] - pred[index]
    rows.loc[index,['modelscore','sub_score']] = [pred[index],sub_score]
rows.to_csv("SVMmodeloutput2.csv", index=False)
r2 = r2_score(y, pred)
print("R²: ", r2)
absolute_error = mean_absolute_error(y, pred)
print("絕對平均誤差:", absolute_error)
mse = mean_squared_error(y, pred)
print("均方誤差: ", mse)

# model = SVR(kernel='rbf', C=10, gamma=0.45)
# R²:  0.6764900587734182
# 絕對平均誤差: 0.9417367942791339
# 均方誤差:  1.4904055018907825

# model = RandomForestRegressor(n_estimators=100, random_state=42)
# R²:  0.6064484913851875
# 絕對平均誤差: 0.9489844284162766
# 均方誤差:  1.8130859641995412