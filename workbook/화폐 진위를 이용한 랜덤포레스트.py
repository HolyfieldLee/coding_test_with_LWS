#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("file:///C:/Users/admin/Downloads/banknote+authentication/data_banknote_authentication.txt", sep=r",", header=None)

df.columns = ["variance", "skewness", "kurtosis", "entropy", "class"]
print("설명: 이 그래프는 위조 지폐를 구분하는 그래프다.")
print("4개의 feature는 각각 분산, 왜도, 첨도, 엔트로피이다")
df



# In[6]:


#A. 라이브러리 소환
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#B. 데이터 소환, 위에 생성된 그래프 (df)를 사용
X = []
y = df['class']
for i in range(1372):
    X.append([df["variance"][i], df["skewness"][i], df["kurtosis"][i], df["entropy"][i]])
    
#C. 훈련 데이터와 테스트 데이터로 나누기
#데이터를 섞어서 훈련용 80%, 테이스용 20%로 나눈다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

#D. 랜덤 포레스트 모델 생성 및 학습
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

#5. 모델 예측 및 평가
#학습이 끝난 모델로 테스트 데이터의 진위을 예측한다.
y_prediction = model.predict(X_test)
#실제 값과 예측 값을 비교하여 정확도를 계산한다.
accuracy = accuracy_score(y_test, y_prediction)
print(f"모델의 정확도 : {accuracy * 100:.2f}%")

#6. 새로운 데이터로 예측해보기
new_flower_data = [[-2.54190, -0.65804, 2.6842, 1.19520]]
pred = model.predict(new_flower_data)
predicted_species = df["class"][pred[0]]
print(f"진위 : {predicted_species }")

