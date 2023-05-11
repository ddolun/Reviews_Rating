from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
import pandas as pd
import numpy as np
import pickle

sentences = []
scores = []
rows = pd.read_csv('test.csv')
i = 0 
for index, row in rows.iterrows():
    sentences.append(row['ckipnlp'])
    scores.append(row['score'])
    i+=1
print("訓練了{}筆資料".format(i))

vector = TfidfVectorizer() 
X =vector.fit_transform(sentences)
y = np.array(scores)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# n_estimators = [50, 100, 150, 200]
# print(" ")
# for n in n_estimators:
#     model = RandomForestRegressor(n_estimators=n, random_state=42)
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     mse = mean_squared_error(y_test, y_pred)
#     r2 = r2_score(y_test, y_pred)
#     absolute_error = mean_absolute_error(y_test, y_pred)
#     r2 = r2_score(y_test, y_pred)
#     print("n_estimators = {}, mse = {}, mae = {} , R² ={}".format(n, mse,absolute_error,r2))
#     print(" ")

model = RandomForestRegressor(n_estimators=120, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error: ", mse)
print("R2 Score: ", r2)
with open('Randommodel.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('Randomvectorizer.pkl', 'wb') as f:
    pickle.dump(vector, f)
