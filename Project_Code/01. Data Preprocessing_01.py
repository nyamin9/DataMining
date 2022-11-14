# 01. 라이브러리 임포트
# 데이터 임포트, 전처리를 위한 pandas, numpy library 임포트
import pandas as pd
import numpy as np

# 시각화를 위한 plotly library 임포트
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()


# 02. 데이터 임포트
# Attributes
# 나이 (일수)
# 성별(1-women, 2-men)
# 키(cm)
# 몸무게(kg)
# ap_hi(systolic blood pressure, 수축혈압)
# ap_lo(diastolic blood pressure, 이완혈압)
# cholesterol(1-normal, 2-above normal, 3-well above normal)
# gluc(혈당)(1-normal, 2-above normal, 3-well above normal)
# smoke(0-비흡연, 1-흡연)
# alco(0-음주X, 1-음주O)
# active(운동여부)(0-X, 1-O)
# Cardio(target)(0-X, 1-O)
cardio = pd.read_csv('C:\\Users\mingu\Desktop\\cardio_train.csv', sep=';')
cardio


# 03. Raw Data Information 확인
# 70000개의 row, cardio 유무(target)를 포함한 13개의 attribute로 이뤄진 dataframe
cardio.info()


# 04. Age 설정
# day기준 age를 year 기준으로 변환 : 365로 나누고 소수점 첫째자리에서 반올림
cardio['age'] = cardio['age'] / 365
cardio['age'] = round(cardio['age'], 0).astype('int64').copy()


# 05. BMI attribute 생성
# BMI = weight / height(m)^2
# BMI 생성 후 사용하지 않을 attribute인 id, height, weight 삭제
cardio['height'] = cardio['height'] / 100
cardio['BMI'] = cardio['weight'] / (cardio['height']**2)
cardio['BMI'] = round(cardio['BMI'], 2).copy()
cardio = cardio.drop(['id','height','weight'], axis = 1)


# 06. Blood Presure 확인
# 수축기혈압(ap_hi)과 이완기혈압(ap_lo) 각각의 info를 확인
# ap_hi / ap_lo attribute 각각 음수값 혹은 지나치게 큰 혈압을 나타내는 outlier를 가지고 있음을 볼 수 있음
pd.DataFrame({'ap_hi' : cardio['ap_hi'].describe(), 'ap_lo' : cardio['ap_lo'].describe()})

# Box plot을 통해 확인 : ap_hi, ap_lo 의 upper_fence, lower_fence 값의 이상 / 이하 값은 outlier로 취급 - 전처리 필요
# ap_hi : upper_fence = 170 / lower_fence = 90
# ap_lo : upper_fence = 105 / lower_fence = 65
# plotly library를 사용해서 Box plot 생성
fig = go.Figure()
fig.add_trace(go.Box(y=cardio['ap_hi'], name = 'ap_hi'))
fig.add_trace(go.Box(y=cardio['ap_lo'], name = 'ap_lo'))

fig.show()

# ap_hi (수축혈압)가 ap_lo (이완혈압)보다 낮은 행 삭제
print(len(cardio[(cardio['ap_hi'] < cardio['ap_lo'])]))
low_drop_index = cardio[(cardio['ap_hi'] < cardio['ap_lo'])].index
cardio = cardio.drop(low_drop_index).copy()
print(len(cardio))

# 수축혈압 전처리
print(len(cardio[(cardio['ap_hi'] < 90) | (cardio['ap_hi'] > 170)]))
drop_index_sys = cardio[(cardio['ap_hi'] < 90) | (cardio['ap_hi'] > 170)].index
cardio = cardio.drop(drop_index_sys).copy()
len(cardio)

# 이완혈압 전처리
print(len(cardio[(cardio['ap_lo'] < 65) | (cardio['ap_lo'] > 105)]))
drop_index_dias = cardio[(cardio['ap_lo'] < 65) | (cardio['ap_lo'] > 105)].index
cardio = cardio.drop(drop_index_dias).copy()
len(cardio)

# Preprocessed data에 대한 Box Plot 
# plotly library를 사용해서 Box plot 생성
fig = go.Figure()
fig.add_trace(go.Box(y=cardio['ap_hi'], name = 'ap_hi'))
fig.add_trace(go.Box(y=cardio['ap_lo'], name = 'ap_lo'))
fig.show() 
