## 01. 라이브러리 설치

import warnings
warnings.filterwarnings('ignore')

# 데이터 임포트 및 전처리를 위한 pandas / numpy library 임포트
import pandas as pd
import numpy as np

# 시각화를 위한 plotly library 임포트
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()

# transaction table 생성
# mlxtend.preprocessing 모듈의 TransactionEncoder 임포트
from mlxtend.preprocessing import TransactionEncoder

# apriori 알고리즘, association_rules 생성 
# mlxtend.frequent_patterns 모듈의 apriori, association_rules 임포트
from mlxtend.frequent_patterns import apriori, association_rules

# 시각화를 위한 seaborn, matplotlib 임포트
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
%matplotlib inline

# PCA 분석을 위한 라이브러리
# PCA 시각화를 위한 plotly.express 모듈 임포트
# PCA 분석 수행을 위한 sklearn.decomposition 모듈의 PCA library 임포트
# PCA 분석을 위한 데이터 표준화 - sklearn.preprocessing 모듈의 StandardScaler library 임포트
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# decision tree를 위한 export_graphviz 라이브러리 임포트
# sklearn 모듈의 tree 라이브러리 임포트
from sklearn.tree import export_graphviz
import graphviz
from sklearn import tree
from os import system    

# 데이터 셋을 train / test 로 분류해주는 라이브러리
from sklearn.model_selection import train_test_split 

# 랜덤포레스트를 위한 데이터 정규화 - StandardScaler 라이브러리
# 랜덤포레스트 생성 RandomForestClassifier 라이브러리
# acuuracy_score 라이브러리 : 정확도 계산 함수
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score 

# ROC Curve, Confusion Matrix, classification report 생성을 위한 라이브러리
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import (
    classification_report, confusion_matrix,
    ConfusionMatrixDisplay)
from enum import Enum


## 02. 데이터 전처리 

cardio = pd.read_csv('C:\\Users\mingu\Desktop\\cardio_train.csv', sep=';')

# day기준 age를 year 기준으로 변환 : 365로 나누고 소수점 첫째자리에서 반올림
cardio['age'] = cardio['age'] / 365
cardio['age'] = round(cardio['age'], 0).astype('int64').copy()

# BMI attribute 생성
cardio['height'] = cardio['height'] / 100
cardio['BMI'] = cardio['weight'] / (cardio['height']**2)
cardio['BMI'] = round(cardio['BMI'], 2).copy()

# id, height, weight attribute 삭제
cardio = cardio.drop(['id','height','weight'], axis = 1)

# 수축기혈압이 이완기혈압보다 낮은 row 삭제
low_drop_index = cardio[(cardio['ap_hi'] < cardio['ap_lo'])].index
cardio = cardio.drop(low_drop_index).copy()

# 90mmHg 이하, 200mmHg 이상의 Ap_hi 혈압 제거
drop_index_sys = cardio[(cardio['ap_hi'] < 90) | (cardio['ap_hi'] > 170)].index
cardio = cardio.drop(drop_index_sys).copy()

# 60mmHg 이하, 140mmHg 이상의 Ap_lo 혈압 제거
drop_index_dias = cardio[(cardio['ap_lo'] < 65) | (cardio['ap_lo'] > 105)].index
cardio = cardio.drop(drop_index_dias).copy()

# target과 feature data 설정
cardio_target = cardio['cardio'].copy()
cardio_target[cardio_target==0] = 'N'
cardio_target[cardio_target==1] = 'Y'
cardio_feat = cardio.drop('cardio',axis = 1)

# PCA Dataframe 출력
# 사용하려는 principal componenet 개수 정의
n_components = 4

pca = PCA(n_components=n_components)
components = pca.fit_transform(cardio)
PCA_df = pd.DataFrame({'PC1' : components[:,0],
             'PC2' : components[:,1],
             'PC3' : components[:,2],
             'PC4' : components[:,3],
             'cardio' : cardio['cardio']})
PCA_df


## 03. Decision Tree
# 트리의 깊이를 늘릴수록 Entropy는 계속 작아지지만 test set에 대한 accuracy는 오히려 감소하는 것을 확인할 수 있었음.

## 03.1 Original Data
cardio.target_rand = cardio['cardio'].copy()
cardio.target_rand[cardio.target_rand==0] = 'N'
cardio.target_rand[cardio.target_rand==1] = 'Y'

cardio_1_feat = cardio.drop(['cardio'], axis = 1).copy() #1. 전체 feature 사용
cardio_2_feat = cardio.drop(['cardio','age','gender','gluc','smoke','alco','active'], axis = 1).copy() #2. [aphi, aplo, cholesterol, BMI]
cardio_3_feat = cardio.drop(['cardio','gender','gluc','smoke','alco','active'], axis = 1).copy() #3. [age, aphi, aplo, cholesterol, BMI]
cardio_4_feat = cardio.drop(['cardio','gender','smoke','alco','active'], axis = 1).copy() #4. [age, aphi, aplo, cholesterol, gluc, BMI]
cardio_5_feat = cardio.drop(['cardio','gender','alco','smoke'], axis = 1).copy() #5. [age, aphi, aplo, cholesterol, gluc, BMI, active]
cardio_6_feat = cardio.drop(['cardio','gender','alco','smoke','age','active'], axis = 1).copy() #6. [aphi, aplo, cholesterol, gluc, BMI]

def predict_accuracy(features, depth):
    x_train, x_test, y_train, y_test = train_test_split(features, cardio.target_rand, test_size=0.3, random_state=1)
    # 데이터 표준화 작업
    sc = StandardScaler()
    sc.fit(x_train)

    # 표준화된 데이터셋
    x_train_std = sc.transform(x_train)
    x_test_std = sc.transform(x_test)

     # 종속변수가 현재 범주형
    clf_train = tree.DecisionTreeClassifier(criterion="entropy",max_depth=depth)
    clf_train = clf_train.fit(x_train,y_train)
    
    # 종속변수가 현재 범주형
    clf_test = tree.DecisionTreeClassifier(criterion="entropy",max_depth=depth)
    clf_test = clf_test.fit(x_train,y_train)

    y_pred_tr_train = clf_train.predict(x_train)
    y_pred_tr_test = clf_test.predict(x_test)
    
    return clf_train, accuracy_score(y_train, y_pred_tr_train), clf_test, accuracy_score(y_test, y_pred_tr_test)
  
  # max_depth = None 인 경우의 train set accuracy와 test set accuracy
print('Case 1 train Accuracy: %.5f' % predict_accuracy(cardio_1_feat, None)[1])
print('Case 1 test Accuracy: %.5f' % predict_accuracy(cardio_1_feat, None)[3], '\n')

print('Case 2 train Accuracy: %.5f' % predict_accuracy(cardio_2_feat, None)[1])
print('Case 2 test Accuracy: %.5f' % predict_accuracy(cardio_2_feat, None)[3], '\n')

print('Case 3 train Accuracy: %.5f' % predict_accuracy(cardio_3_feat, None)[1])
print('Case 3 test Accuracy: %.5f' % predict_accuracy(cardio_3_feat, None)[3], '\n')

print('Case 4 train Accuracy: %.5f' % predict_accuracy(cardio_4_feat, None)[1])
print('Case 4 test Accuracy: %.5f' % predict_accuracy(cardio_4_feat, None)[3], '\n')

print('Case 5 train Accuracy: %.5f' % predict_accuracy(cardio_5_feat, None)[1])
print('Case 5 test Accuracy: %.5f' % predict_accuracy(cardio_5_feat, None)[3], '\n')

print('Case 6 train Accuracy: %.5f' % predict_accuracy(cardio_6_feat, None)[1])
print('Case 6 test Accuracy: %.5f' % predict_accuracy(cardio_6_feat, None)[3], '\n')

# max_depth = 5 인 경우의 train set accuracy와 test set accuracy
print('Case 1 train Accuracy: %.5f' % predict_accuracy(cardio_1_feat, 5)[1])
print('Case 1 test Accuracy: %.5f' % predict_accuracy(cardio_1_feat, 5)[3], '\n')

print('Case 2 train Accuracy: %.5f' % predict_accuracy(cardio_2_feat, 5)[1])
print('Case 2 test Accuracy: %.5f' % predict_accuracy(cardio_2_feat, 5)[3], '\n')

print('Case 3 train Accuracy: %.5f' % predict_accuracy(cardio_3_feat, 5)[1])
print('Case 3 test Accuracy: %.5f' % predict_accuracy(cardio_3_feat, 5)[3], '\n')

print('Case 4 train Accuracy: %.5f' % predict_accuracy(cardio_4_feat, 5)[1])
print('Case 4 test Accuracy: %.5f' % predict_accuracy(cardio_4_feat, 5)[3], '\n')

print('Case 5 train Accuracy: %.5f' % predict_accuracy(cardio_5_feat, 5)[1])
print('Case 5 test Accuracy: %.5f' % predict_accuracy(cardio_5_feat, 5)[3], '\n')

print('Case 6 train Accuracy: %.5f' % predict_accuracy(cardio_6_feat, 5)[1])
print('Case 6 test Accuracy: %.5f' % predict_accuracy(cardio_6_feat, 5)[3], '\n')

## 03.2 PCA
PCA_df.target = PCA_df['cardio'].copy()
PCA_df.target[PCA_df.target==0] = 'N'
PCA_df.target[PCA_df.target==1] = 'Y'
PCA_df.feat = PCA_df.drop(['cardio'], axis = 1).copy()

x_train_PCA, x_test_PCA, y_train_PCA, y_test_PCA = train_test_split(PCA_df.feat, PCA_df.target, test_size=0.2, random_state=1)
clf_PCA = tree.DecisionTreeClassifier(criterion = "entropy", max_depth=6)  # Information Gain - entropy
clf_PCA = clf_PCA.fit(x_train_PCA, y_train_PCA)  

# 깊이에 따른 accuracy 시각화
accuracy_df = pd.DataFrame()
for i in range(1,20):
    a = tree.DecisionTreeClassifier(criterion = "entropy", max_depth=i)
    a = a.fit(x_train_PCA, y_train_PCA)  
    b = a.predict(x_test_PCA)
    accuracy_df =  accuracy_df.append(pd.DataFrame({'accuracy' : (accuracy_score(y_test_PCA, b)).round(5)}, index = [i]))
    
px.line(
    x=range(1,20),
    y=accuracy_df['accuracy'],
    labels={"x": "max_depth", "y": "Accuracy"}
)

# max_depth = 6 인 경우의 train set / test set accuracy
y_pred_tr_PCA_test = clf_PCA.predict(x_test_PCA)
y_pred_tr_PCA_train = clf_PCA.predict(x_train_PCA)
print('PCA train Accuracy: %.5f' % accuracy_score(y_train_PCA, y_pred_tr_PCA_train))
print('PCA test Accuracy: %.5f' % accuracy_score(y_test_PCA, y_pred_tr_PCA_test))


## 04. Decision Tree 시각화

# 결정트리를 png 형태로 저장하기 위한 라이브러리 임포트
import pydotplus

## 04.1 attribute set 4에 대한 결정트리 시각화 (max_depth = 5)
dot_data = tree.export_graphviz(predict_accuracy(cardio_4_feat, 5)[0],        # 의사결정나무 모형 대입
                               out_file = None,     # file로 변환할 것인가
                               feature_names = cardio_4_feat.columns, # feature 이름
                               class_names = cardio.target_rand,   # target 이름
                               filled = True,        # 그림에 색상을 넣을것인가
                               rounded = True,       # 반올림을 진행할 것인가
                               special_characters = True)    # 특수문자를 사용하나

graph = pydotplus.graph_from_dot_data(dot_data)
graph.set_size('"60,30!"')
graph.write_png('atribute_4_tree.png')


## 04.2 PCA Dataframe에 대한 결정트리 시각화 (max_depth = 6)
dot_data_PCA = tree.export_graphviz(clf_PCA,        # 의사결정나무 모형 대입
                               out_file = None,     # file로 변환할 것인가
                               feature_names = PCA_df.feat.columns, # feature 이름
                               class_names = PCA_df.target,   # target 이름
                               filled = True,        # 그림에 색상을 넣을것인가
                               rounded = True,       # 반올림을 진행할 것인가
                               special_characters = True)    # 특수문자를 사용하나

graph_PCA = pydotplus.graph_from_dot_data(dot_data_PCA)
graph_PCA.set_size('"60,30!"')
graph_PCA.write_png('PCA_tree.png')


## 05. Random Forest

## 05.1 Original Data

## 05.1.1 attribute set 5를 사용한 경우
cardio.target_out = cardio['cardio'].copy()
cardio.feat_out = cardio.drop(['cardio','gender','alco','smoke'], axis = 1).copy()

train_x_out, test_x_out, train_y_out, test_y_out = train_test_split(cardio.feat_out, cardio.target_out, test_size=0.3, random_state=0)

# 데이터 표준화 작업
sc = StandardScaler()
sc.fit(train_x_out)

# 표준화된 데이터셋
train_x_out_std = sc.transform(train_x_out)
test_x_out_std = sc.transform(test_x_out)

clf = RandomForestClassifier(random_state=0, max_depth = 12, n_estimators = 200)
clf.fit(train_x_out,train_y_out)

predict6 = clf.predict(train_x_out)
predict5 = clf.predict(test_x_out)

print("Train set accuracy : ", accuracy_score(train_y_out, predict6))
print("Test set accuracy : ", accuracy_score(test_y_out,predict5))


## 05.1.2 original data의 모든 attribute를 사용한 경우 : case 1
cardio.target_all = cardio['cardio'].copy()
cardio.feat_all = cardio.drop(['cardio'], axis = 1).copy()

train_x_all, test_x_all, train_y_all, test_y_all = train_test_split(cardio.feat_all, cardio.target_all, test_size=0.3, random_state=0)

# 데이터 표준화 작업
sc = StandardScaler()
sc.fit(train_x_all)

# 표준화된 데이터셋
train_x_std_all = sc.transform(train_x_all)
test_x_std_all = sc.transform(test_x_all)

clf = RandomForestClassifier(random_state=0, max_depth = 12, n_estimators = 200)
clf.fit(train_x_all,train_y_all)

predict4 = clf.predict(train_x_all)
predict3 = clf.predict(test_x_all)

print("Train set accuracy : ", accuracy_score(train_y_all, predict4))
print("Test set accuracy : ", accuracy_score(test_y_all,predict3))

### ROC Curve
# 전체 attribute를 사용한 경우의 ROC curve 출력
fpr_tr, tpr_tr, ths_tr = roc_curve(test_y_all, predict3)
auc_tr = auc(fpr_tr, tpr_tr)

fig = plt.figure(figsize = (8,4))
plt.subplot(121)
plt.plot(fpr_tr, tpr_tr, 
        lw=3, label='ROC curve (area = %0.2f)' % auc_tr)
plt.plot([0, 1], [0, 1], color='skyblue', lw=2,linestyle='--')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.legend(loc="lower right", prop={'size' : 10})
plt.title('validation set')
plt.show()

### Confusion Matrix
# 전체 attribute를 사용한 경우의 confusion matrix 출력
class Diagnosis(Enum):
    No_Cardio = 0
    Cardio = 1    
    
cm = confusion_matrix(
    test_y_all,
    (predict3>.5).astype(np.int8),
#    normalize='true',
)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[d.name for d in Diagnosis],
)
disp.plot(ax=plt.subplots(1, 1, facecolor='white')[1], cmap=plt.cm.Reds)


## 05.2 PCA

PCA_df_target = PCA_df['cardio']
PCA_df_feat = PCA_df.drop(['cardio'],axis = 1)

train_x_PCA, test_x_PCA, train_y_PCA, test_y_PCA = train_test_split(PCA_df_feat, PCA_df_target, test_size=0.3, random_state=1)
print(train_x_PCA.shape, test_x_PCA.shape, train_y_PCA.shape, test_y_PCA.shape)

clf = RandomForestClassifier(random_state=1)
clf.fit(train_x_PCA,train_y_PCA)

predict2 = clf.predict(train_x_PCA)
predict1 = clf.predict(test_x_PCA)

print("Train set accuracy : ", accuracy_score(train_y_PCA, predict2))
print("Test set accuracy : ", accuracy_score(test_y_PCA,predict1))

### ROC Curve
# PCA DataFrame을 사용한 경우의 ROC curve 출력
fpr_tr, tpr_tr, ths_tr = roc_curve(test_y_PCA, predict1)
auc_tr = auc(fpr_tr, tpr_tr)

fig = plt.figure(figsize = (8,4))
plt.subplot(121)
plt.plot(fpr_tr, tpr_tr, 
        lw=3, label='ROC curve (area = %0.2f)' % auc_tr)
plt.plot([0, 1], [0, 1], color='skyblue', lw=2,linestyle='--')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.legend(loc="lower right", prop={'size' : 10})
plt.title('validation set')
plt.show()

### Confusion Matrix
# PCA DataFrame을 사용한 경우의 confusion matrix 출력
class Diagnosis(Enum):
    No_Cardio = 0
    Cardio = 1    
    
cm = confusion_matrix(
    test_y_PCA,
    (predict1>.5).astype(np.int8),
#    normalize='true',
)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[d.name for d in Diagnosis],
)
disp.plot(ax=plt.subplots(1, 1, facecolor='white')[1], cmap=plt.cm.Blues)
