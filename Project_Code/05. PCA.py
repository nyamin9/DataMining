# 01. 라이브러리 임포트
# 데이터 임포트 및 전처리를 위한 pandas / numpy library 임포트
import pandas as pd
import numpy as np

# 시각화를 위한 plotly library 임포트
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()

import chart_studio
import chart_studio.plotly as py
import cufflinks as cf

cf.go_offline(connected = True)
import chart_studio.tools as tls

pd.options.plotting.backend = 'plotly'
import plotly.io as pio
pio.renderers.default = "notebook_connected"

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


# 02. 데이터 전처리
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

cardio


# 03. target과 feature data 설정
cardio_target = cardio['cardio'].copy()
cardio_target[cardio_target==0] = 'N'
cardio_target[cardio_target==1] = 'Y'
cardio_feat = cardio.drop('cardio',axis = 1)


# 04. PCA(01) : dimension = 3
# sklearn.decomposition 모듈의 PCA library 임포트
# pca.fit_transform() : cardio[features]를 scaling 한 뒤에 principal component로 변환
# pca.explained_variance_ratio_ : dimension에 따른 variance 설명 정도
pca = PCA()
components = pca.fit_transform(cardio_feat)

# PCA 결과 시각화
labels = {
    str(i): f"PC {i+1} ({var:.1f}%)"
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}

fig = px.scatter_matrix(
    components,
    labels=labels,
    dimensions=range(3),
    color=cardio_target, opacity = 0.5
)
fig.update_traces(diagonal_visible=False)
fig.show()


# 05. dimension에 따른 variance 설명 정도의 누적합 시각화
pca = PCA()
pca.fit(cardio)
exp_var_cumul = np.cumsum(pca.explained_variance_ratio_)

px.area(
    x=range(1, exp_var_cumul.shape[0] + 1),
    y=exp_var_cumul,
    labels={"x": "# Components", "y": "Explained Variance"}
)


# 06. PCA(02) : dimension = 4
# 사용하려는 principal componenet 개수 정의
n_components = 4

# sklearn.decomposition 모듈의 PCA library 임포트. principal componenet 개수 정의.
# pca.fit_transform() : cardio[features]를 scaling 한 뒤에 principal component로 변환
# pca.explained_variance_ratio_ : dimension에 따른 variance 설명 정도
pca = PCA(n_components=n_components)
components = pca.fit_transform(cardio)

# PCA 결과 시각화
total_var = pca.explained_variance_ratio_.sum() * 100

labels = {str(i): f"PC {i+1}" for i in range(n_components)}

fig = px.scatter_matrix(
    components,
    color=cardio_target,
    opacity = 0.5,
    dimensions=range(n_components),
    labels=labels,
    title=f'Total Explained Variance: {total_var:.2f}%',
)
fig.update_traces(diagonal_visible=False)
fig.show()


# 06. vardiance를 설명하는 데 사용된 original attribute vector의 방향성 파악
X = cardio[cardio_feat.columns]

pca = PCA(n_components=4)
components = pca.fit_transform(X)

loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

fig = px.scatter(components, x=0, y=1, color=cardio_target, opacity = 0.5)

for i, feature in enumerate(X):
    fig.add_shape(
        type='line',
        x0=0, y0=0,
        x1=loadings[i, 0],
        y1=loadings[i, 1],
        line=dict(color="springgreen",width=3.5)
    )
    fig.add_annotation(
        x=loadings[i, 0],
        y=loadings[i, 1],
        ax=0, ay=0,
        xanchor="center",
        yanchor="bottom",
        text=feature,
        font = {'color':'white'},
        bgcolor = 'grey'
    )
fig.show()


# 07. PCA Dataframe 출력
pca = PCA(n_components=n_components)
components = pca.fit_transform(cardio)
PCA_df = pd.DataFrame({'PC1' : components[:,0],
             'PC2' : components[:,1],
             'PC3' : components[:,2],
             'PC4' : components[:,3],
             'cardio' : cardio['cardio']})
PCA_df
