# 라이브러리 임포트
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


# 02. 데이터 전처리 과정 요약 코드
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


# 03. 상관관계 분석
plt.figure(figsize = (20,12))
ax = sns.heatmap(cardio.corr(), annot=True, annot_kws=dict(color='r'), cmap='Greens')
plt.show()


# 04. Support / Confidence / Lift를 통한 correlation 분석

# 04.1
# BMI attribute를 위한 categorize 함수 생성
# BMI < 18.5 : 저체중
# 18.5 =< BMI < 25 : 정상
# 25 =< BMI < 30 : 과체중
# 30 =< BMI < 39.9 : 비만
# 39.9 =< BMI  : 고도비만S
def bmi(x):
    if x < 18.5:
        x = 'LOW'
    elif (x >= 18.5) & (x<25):
        x = 'NORMAL'
    elif (x >= 25) & (x < 30):
        x = 'OVER'
    elif (x >= 30) & (x < 39.9):
        x = 'OBESITY'
    else:
        x = 'HIGH_OBESITY'
    return x

# 04.2  
# cardio 데이터 범주화
pre_tran = cardio.copy()

# gender : 1 2
pre_tran = pre_tran.replace({'gender':1},'Women')
pre_tran = pre_tran.replace({'gender':2},'Men')

# cholesterol : 1 2 3
pre_tran = pre_tran.replace({'cholesterol':1},'Normal_cho')
pre_tran = pre_tran.replace({'cholesterol':2},'Above_Normal_cho')
pre_tran = pre_tran.replace({'cholesterol':3},'Well_Above_Normal_cho')

# gluc : 1 2 3
pre_tran = pre_tran.replace({'gluc':1},'Normal_gluc')
pre_tran = pre_tran.replace({'gluc':2},'Above_Normal_gluc')
pre_tran = pre_tran.replace({'gluc':3},'Well_Above_Normal_gluc')

# smoke : 0 1
pre_tran = pre_tran.replace({'smoke':0},'No_Smoke')
pre_tran = pre_tran.replace({'smoke':1},'Smoke')

# alco : 0 1
pre_tran = pre_tran.replace({'alco':0},'No_Alcohol')
pre_tran = pre_tran.replace({'alco':1},'Alcohol')

# active : 0 1
pre_tran = pre_tran.replace({'active':0},'No_Active')
pre_tran = pre_tran.replace({'active':1},'Active')

# cardio : 0 1, target
pre_tran = pre_tran.replace({'cardio':0},'No_cardio')
pre_tran = pre_tran.replace({'cardio':1},'Cardio')

# ap_hi가 140이상이면 HBP_SYS(고혈압), 그 외에는 NBP_SYS(정상)
# ap_lork 90 이상이면 HBP_DIAS(고혈압), 그 외에는 NBP_DIAS(정상)
pre_tran["ap_hi"] = np.where(pre_tran["ap_hi"] >=140, 'HBP_SYS', 'NBP_SYS')
pre_tran["ap_lo"] = np.where(pre_tran["ap_lo"] >=90, 'HBP_DIAS', 'NBP_DIAS')

# age : 연령대로 분류
pre_tran.loc[pre_tran['age'] // 10 == 3, 'age'] = 30
pre_tran.loc[pre_tran['age'] // 10 == 4, 'age'] = 40
pre_tran.loc[pre_tran['age'] // 10 == 5, 'age'] = 50
pre_tran.loc[pre_tran['age'] // 10 == 6, 'age'] = 60

# BMI : 앞서 생성한 BMI 함수 사용
pre_tran['BMI'] = pre_tran['BMI'].apply(bmi)

print('row : ', len(pre_tran))
print('columns : ', len(pre_tran.columns))
pre_tran.head()

# 04.3
# transaction 데이터 생성
# 범주형 데이터를 mlxtend 메소드의 transform 함수에 넣기 위해 list형태로 변환 : trans_data
trans_data = np.array(pre_tran)
trans_data = np.array(trans_data.tolist())

# transform() 함수로 trans_data가 one-hot encoding 된 형태의 boolean list를 te_ary로 받음
# te_ary를 데이터프레임 형태로 변환하여 transaction data 생성 
# transaction : attribute의 각 category에 대한 value를 column으로 받음
te = TransactionEncoder()
te_ary = te.fit(trans_data).transform(trans_data)
transaction = pd.DataFrame(te_ary, columns=te.columns_)
transaction

# 04.4 - Age / Cardio
# pre_tran dataframe으로부터 원하는 attribute만을 추출
# 해당하는 attribute의 category에 대한 transaction dataframe 생성
Age_C = pre_tran[['age','cardio']]

train_data_Age_C = np.array(Age_C)
train_data_Age_C = np.array(train_data_Age_C.tolist())

te = TransactionEncoder()
te_Age_C = te.fit(train_data_Age_C).transform(train_data_Age_C)
transaction_Age_C = pd.DataFrame(te_Age_C, columns=te.columns_)

# mlxtend.frequent_patterns 모듈의 apriori, association_rules 함수
# apriori() : itemsets 간의 Support를 계산하여 dataframe으로 반환 - 설정한 min_support를 만족하는 경우만 반환
# association_rules() : antecedents(선행)과 consequents(후행)의 순서를 고려하여 support, confidence, lift, leverage, conviction dataframe 반환
# association_rules() 함수의 metric, min_threshold 옵션 : 설정한 metric이 min_threshold 이상인 경우만 반환
frequent_itemsets_Age_C = apriori(transaction_Age_C, min_support=0.000001,use_colnames=True)
frequent_itemsets_Age_C = frequent_itemsets_Age_C.sort_values('support',ascending = False)
rule_Age_C = association_rules(frequent_itemsets_Age_C, metric="lift", min_threshold=0)

# cardio와 영향을 미치는 attribute 간의 인과관계를 알아보기 위해 cardio를 consequents로 하는 경우를 반환하도록 설정
# confidence가 큰 순서대로 출력
y = rule_Age_C['consequents'].apply(lambda rule_Age_C: "Cardio" in str(rule_Age_C))
y = y[y==True].index
rule_Age_C_cardio = rule_Age_C.loc[y].sort_values('confidence', ascending = False)
rule_Age_C_cardio

# 시각화
fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['60','50','40','30'], y = rule_Age_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Age_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15)) # Support를 scatter하는 부분

fig.add_trace(
    go.Scatter(
    x = ['60','50','40','30'], y = rule_Age_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Age_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15)) # Confidence를 scatter하는 부분

fig.add_trace(
    go.Scatter(
    x = ['60','50','40','30'], y = rule_Age_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Age_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15)) # Lift를 scatter하는 부분

# Lift 판단 기준(Lift > 1)을 나타내기 위한 수직선 plot
fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="        Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )
# support 판단 기준(support > 0.01)을 나타내기 위한 수직선 plot
fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="        support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )
# confidence 판단 기준(confidence > 0.6)을 나타내기 위한 수직선 plot
fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="        confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Age-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Age', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.5 - Gender / Cardio
# 전자와 동일
Gender_C = pre_tran[['gender','cardio']]

train_data_Gender_C = np.array(Gender_C)
train_data_Gender_C = np.array(train_data_Gender_C.tolist())

te = TransactionEncoder()
te_Gender_C = te.fit(train_data_Gender_C).transform(train_data_Gender_C)
transaction_Gender_C = pd.DataFrame(te_Gender_C, columns=te.columns_)

frequent_itemsets_Gender_C = apriori(transaction_Gender_C, min_support=0.0000001,use_colnames=True)
frequent_itemsets_Gender_C = frequent_itemsets_Gender_C.sort_values('support',ascending = False)
rule_Gender_C = association_rules(frequent_itemsets_Gender_C, metric="lift", min_threshold=0)

y = rule_Gender_C['consequents'].apply(lambda rule_Gender_C: "Cardio" in str(rule_Gender_C))
y = y[y==True].index
rule_Gender_C_cardio = rule_Gender_C.loc[y].sort_values('confidence', ascending = False)
rule_Gender_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['Women','Men'], y = rule_Gender_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Gender_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['Women','Men'], y = rule_Gender_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Gender_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['Women','Men'], y = rule_Gender_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Gender_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Gender-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Gender', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.6 - Systolic / Cardio
# 전자와 동일
Sys_C = pre_tran[['ap_hi','cardio']]

train_data_Sys_C = np.array(Sys_C)
train_data_Sys_C = np.array(train_data_Sys_C.tolist())

te = TransactionEncoder()
te_Sys_C = te.fit(train_data_Sys_C).transform(train_data_Sys_C)
transaction_Sys_C = pd.DataFrame(te_Sys_C, columns=te.columns_)

frequent_itemsets_Sys_C = apriori(transaction_Sys_C, min_support=0.000001,use_colnames=True)
frequent_itemsets_Sys_C = frequent_itemsets_Sys_C.sort_values('support',ascending = False)
rule_Sys_C = association_rules(frequent_itemsets_Sys_C, metric="lift", min_threshold=0)

y = rule_Sys_C['consequents'].apply(lambda rule_Sys_C: "Cardio" in str(rule_Sys_C))
y = y[y==True].index
rule_Sys_C_cardio = rule_Sys_C.loc[y].sort_values('confidence', ascending = False)
rule_Sys_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['HBP_SYS','NBP_SYS'], y = rule_Sys_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Sys_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['HBP_SYS','NBP_SYS'], y = rule_Sys_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Sys_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['HBP_SYS','NBP_SYS'], y = rule_Sys_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Sys_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Ap_hi-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Ap_hi', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.7 - Diastolic / Cardio
# 전자와 동일
Dias_C = pre_tran[['ap_lo','cardio']]

train_data_Dias_C = np.array(Dias_C)
train_data_Dias_C = np.array(train_data_Dias_C.tolist())

te = TransactionEncoder()
te_Dias_C = te.fit(train_data_Dias_C).transform(train_data_Dias_C)
transaction_Dias_C = pd.DataFrame(te_Dias_C, columns=te.columns_)

frequent_itemsets_Dias_C = apriori(transaction_Dias_C, min_support=0.0001,use_colnames=True)
frequent_itemsets_Dias_C = frequent_itemsets_Dias_C.sort_values('support',ascending = False)
rule_Dias_C = association_rules(frequent_itemsets_Dias_C, metric="lift", min_threshold=0)

y = rule_Dias_C['consequents'].apply(lambda rule_Dias_C: "Cardio" in str(rule_Dias_C))
y = y[y==True].index
rule_Dias_C_cardio = rule_Dias_C.loc[y].sort_values('confidence', ascending = False)
rule_Dias_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['HBP_DIAS','NBP_DIAS'], y = rule_Dias_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Dias_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['HBP_DIAS','NBP_DIAS'], y = rule_Dias_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Dias_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['HBP_DIAS','NBP_DIAS'], y = rule_Dias_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Dias_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Ap_lo-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Ap_lo', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()


# 04.8 - Cholesterol / Cardio
# 전자와 동일
Chol_C = pre_tran[['cholesterol','cardio']]

train_data_Chol_C = np.array(Chol_C)
train_data_Chol_C = np.array(train_data_Chol_C.tolist())

te = TransactionEncoder()
te_Chol_C = te.fit(train_data_Chol_C).transform(train_data_Chol_C)
transaction_Chol_C = pd.DataFrame(te_Chol_C, columns=te.columns_)

frequent_itemsets_Chol_C = apriori(transaction_Chol_C, min_support=0.0001,use_colnames=True)
frequent_itemsets_Chol_C = frequent_itemsets_Chol_C.sort_values('support',ascending = False)
rule_Chol_C = association_rules(frequent_itemsets_Chol_C, metric="lift", min_threshold=0)

y = rule_Chol_C['consequents'].apply(lambda rule_Chol_C: "Cardio" in str(rule_Chol_C))
y = y[y==True].index
rule_Chol_C_cardio = rule_Chol_C.loc[y].sort_values('confidence', ascending = False)
rule_Chol_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['Well_Above_Normal_cho','Above_Normal_cho','Normal_cho'], y = rule_Chol_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Chol_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['Well_Above_Normal_cho','Above_Normal_cho','Normal_cho'], y = rule_Chol_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Chol_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['Well_Above_Normal_cho','Above_Normal_cho','Normal_cho'], y = rule_Chol_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Chol_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Cholesterol-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Cholesterol', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.9 - Glucose / Cardio
# 전자와 동일
Gluc_C = pre_tran[['gluc','cardio']]

train_data_Gluc_C = np.array(Gluc_C)
train_data_Gluc_C = np.array(train_data_Gluc_C.tolist())

te = TransactionEncoder()
te_Gluc_C = te.fit(train_data_Gluc_C).transform(train_data_Gluc_C)
transaction_Gluc_C = pd.DataFrame(te_Gluc_C, columns=te.columns_)

frequent_itemsets_Gluc_C = apriori(transaction_Gluc_C, min_support=0.0001,use_colnames=True)
frequent_itemsets_Gluc_C = frequent_itemsets_Gluc_C.sort_values('support',ascending = False)
rule_Gluc_C = association_rules(frequent_itemsets_Gluc_C, metric="lift", min_threshold=0)

y = rule_Gluc_C['consequents'].apply(lambda rule_Gluc_C: "Cardio" in str(rule_Gluc_C))
y = y[y==True].index
rule_Gluc_C_cardio = rule_Gluc_C.loc[y].sort_values('confidence', ascending = False)
rule_Gluc_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['Well_Above_Normal_gluc','Above_Normal_gluc','Normal_gluc'], y = rule_Gluc_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Gluc_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['Well_Above_Normal_gluc','Above_Normal_gluc','Normal_gluc'], y = rule_Gluc_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Gluc_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['Well_Above_Normal_gluc','Above_Normal_gluc','Normal_gluc'], y = rule_Gluc_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Gluc_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Glucose-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Glucose', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.10 - Smoke / Cardio
# 전자와 동일
Smoke_C = pre_tran[['smoke','cardio']]

train_data_Smoke_C = np.array(Smoke_C)
train_data_Smoke_C = np.array(train_data_Smoke_C.tolist())

te = TransactionEncoder()
te_Smoke_C = te.fit(train_data_Smoke_C).transform(train_data_Smoke_C)
transaction_Smoke_C = pd.DataFrame(te_Smoke_C, columns=te.columns_)

frequent_itemsets_Smoke_C = apriori(transaction_Smoke_C, min_support=0.0001,use_colnames=True)
frequent_itemsets_Smoke_C = frequent_itemsets_Smoke_C.sort_values('support',ascending = False)
rule_Smoke_C = association_rules(frequent_itemsets_Smoke_C, metric="lift", min_threshold=0)

y = rule_Smoke_C['consequents'].apply(lambda rule_Smoke_C: "Cardio" in str(rule_Smoke_C))
y = y[y==True].index
rule_Smoke_C_cardio = rule_Smoke_C.loc[y].sort_values('confidence', ascending = False)
rule_Smoke_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['No_Smoke','Smoke'], y = rule_Smoke_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Smoke_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['No_Smoke','Smoke'], y = rule_Smoke_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Smoke_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['No_Smoke','Smoke'], y = rule_Smoke_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Smoke_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Smoke-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Smoke', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.11 - Alcohol / Cardio
# 전자와 동일
Alco_C = pre_tran[['alco','cardio']]

train_data_Alco_C = np.array(Alco_C)
train_data_Alco_C = np.array(train_data_Alco_C.tolist())

te = TransactionEncoder()
te_Alco_C = te.fit(train_data_Alco_C).transform(train_data_Alco_C)
transaction_Alco_C = pd.DataFrame(te_Alco_C, columns=te.columns_)

frequent_itemsets_Alco_C = apriori(transaction_Alco_C, min_support=0.0001,use_colnames=True)
frequent_itemsets_Alco_C = frequent_itemsets_Alco_C.sort_values('support',ascending = False)
rule_Alco_C = association_rules(frequent_itemsets_Alco_C, metric="lift", min_threshold=0)

y = rule_Alco_C['consequents'].apply(lambda rule_Alco_C: "Cardio" in str(rule_Alco_C))
y = y[y==True].index
rule_Alco_C_cardio = rule_Alco_C.loc[y].sort_values('confidence', ascending = False)
rule_Alco_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['No_Alcohol','Alcohol'], y = rule_Alco_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Alco_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['No_Alcohol','Alcohol'], y = rule_Alco_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Alco_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['No_Alcohol','Alcohol'], y = rule_Alco_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Alco_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Alcohol-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Alcohol', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.12 - Activation / Cardio
# 전자와 동일
Act_C = pre_tran[['active','cardio']]

train_data_Act_C = np.array(Act_C)
train_data_Act_C = np.array(train_data_Act_C.tolist())

te = TransactionEncoder()
te_Act_C = te.fit(train_data_Act_C).transform(train_data_Act_C)
transaction_Act_C = pd.DataFrame(te_Act_C, columns=te.columns_)

frequent_itemsets_Act_C = apriori(transaction_Act_C, min_support=0.0001,use_colnames=True)
frequent_itemsets_Act_C = frequent_itemsets_Act_C.sort_values('support',ascending = False)
rule_Act_C = association_rules(frequent_itemsets_Act_C, metric="lift", min_threshold=0)

y = rule_Act_C['consequents'].apply(lambda rule_Act_C: "Cardio" in str(rule_Act_C))
y = y[y==True].index
rule_Act_C_cardio = rule_Act_C.loc[y].sort_values('confidence', ascending = False)
rule_Act_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['No_Active','Active'], y = rule_Act_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Act_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['No_Active','Active'], y = rule_Act_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Act_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['No_Active','Active'], y = rule_Act_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_Act_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'Active-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'Active', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()

# 04.13 - BMI / Cardio
# 전자와 동일
BMI_C = pre_tran[['BMI','cardio']]

train_data_BMI_C = np.array(BMI_C)
train_data_BMI_C = np.array(train_data_BMI_C.tolist())

te = TransactionEncoder()
te_BMI_C = te.fit(train_data_BMI_C).transform(train_data_BMI_C)
transaction_BMI_C = pd.DataFrame(te_BMI_C, columns=te.columns_)

frequent_itemsets_BMI_C = apriori(transaction_BMI_C, min_support=0.0001,use_colnames=True)
frequent_itemsets_BMI_C = frequent_itemsets_BMI_C.sort_values('support',ascending = False)
rule_BMI_C = association_rules(frequent_itemsets_BMI_C, metric="lift", min_threshold=0)

y = rule_BMI_C['consequents'].apply(lambda rule_BMI_C: "Cardio" in str(rule_BMI_C))
y = y[y==True].index
rule_BMI_C_cardio = rule_BMI_C.loc[y].sort_values('confidence', ascending = False)
rule_BMI_C_cardio

fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = ['HIGH_OBESITY','OBESITY','OVER','NORMAL','LOW'], y = rule_BMI_C_cardio['support'], name = 'Support', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_BMI_C_cardio['support'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['HIGH_OBESITY','OBESITY','OVER','NORMAL','LOW'], y = rule_BMI_C_cardio['confidence'], name = 'Confidence', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_BMI_C_cardio['confidence'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_trace(
    go.Scatter(
    x = ['HIGH_OBESITY','OBESITY','OVER','NORMAL','LOW'], y = rule_BMI_C_cardio['lift'], name = 'Lift', 
        mode = 'markers+text', marker_size = 20, 
        text = rule_BMI_C_cardio['lift'].round(3), textposition = 'middle right', textfont_size = 15))

fig.add_hline(y=1, line_dash="dot",
              line_color = "#1dd1ad",
              annotation_text="    Lift > 1", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.01, line_dash="dot",
              line_color = "#8c8cf5",
              annotation_text="    support > 0.01", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.add_hline(y=0.6, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="    confidence > 0.6", 
              annotation_position="bottom left",
              annotation_font_size=17,
              annotation_font_color="gray"
             )

fig.update_layout(
    {
        'title' : {'text':'BMI-Cardio 별 Support, Confidence, Lift 값', 'font':{'size' : 25}},
        'xaxis' : {'title':{'text' : 'BMI', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        'yaxis' : {'title':{'text' : 'Support / Confidence / Lift', 'font':{'size' : 20}}, 'showticklabels':True, 'tickfont' : {'size' : 15}},
        
        'template' : 'plotly_dark'
    })

fig.show()
