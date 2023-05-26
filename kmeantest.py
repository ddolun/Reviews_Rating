# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn import metrics
# from sklearn.cluster import KMeans
# from scipy.sparse import csr_matrix
# from sklearn.feature_extraction.text import TfidfVectorizer

# sentences = []
# scores = []
# rows = pd.read_csv('test.csv')
# i = 0 
# for index, row in rows.iterrows():
#     sentences.append(str(row['ckipnlp']))
#     scores.append(row['score'])
#     i+=1
# print("訓練了{}筆資料".format(i))

# # 特征提取
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(sentences).toarray()
# print(type(X))
# new_X = csr_matrix(X)

# # 聚类分析
# kmeans = KMeans(n_clusters=8, random_state=42).fit(new_X)

# # 输出聚类结果
# print(kmeans.labels_)
# y_pred = KMeans(n_clusters=10, random_state=9).fit_predict(new_X)
#------------------------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.svm import SVR
import pandas as pd
import pickle
sentences = []
scores = []
rows = pd.read_csv('test3.csv')
i = 0 
for index, row in rows.iterrows():
    sentences.(row['ckipnlp'])
    scores.append(row['score'])
    i+=1
print("訓練了{}筆資料".format(i))
# 將中文句子轉換為詞向量
vector = TfidfVectorizer() 
X = vector.fit_transform(sentences)
y = np.array(scores)
# 切分訓練集和測試集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 建立 SVM 回歸模型
model = SVR(kernel='rbf', C=10, gamma=0.45)

# 訓練及儲存模型
model.fit(X, y)
with open('117kmodel.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('117kvectorizer.pkl', 'wb') as f:
    pickle.dump(vector, f)


# 預測測試集的評分
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("MSE: ", mse)
# print("R²: ", r2)

# 輸出結果
# for i in range(len(y_pred)):
# for i in range(150):
#     print("預測結果：{}，實際結果：{}".format(y_pred[i], y_test[i]))