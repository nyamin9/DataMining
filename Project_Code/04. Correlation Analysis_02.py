# 범주화된 데이터 확인
pre_tran.head(2)

# 트랜잭션 데이터 확인
transaction.head(2)


# 01. chi-square 계산(original cardio dataframe의 attribute 기준)
# scipy.stats의 chi2_contingency를 통해서 contingency table 생성.
# contingency table을 바탕으로 chi-square와 p-value 계산.
pre_tran_2 = pre_tran.drop('cardio', axis = 1)
chi_list_origin = pd.DataFrame()
from scipy.stats import chi2_contingency
for i in range(len(pre_tran_2.columns)):
    f=pre_tran_2.columns[i]
    contigency = pd.crosstab(pre_tran_2[f],pre_tran['cardio'])
    chi, p, dof, expected = chi2_contingency(contigency)
    chi_list_origin = chi_list_origin.append((pd.DataFrame({'chi' :chi, 'p-value':p}, index = [pre_tran_2.columns[i]+" & cardio"])))
chi_list_origin = chi_list_origin.sort_values('chi', ascending = False)
chi_list_origin

# Category Data 기준 Attribute의 Cardio와의 chi-square 연산 결과 시각화
fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = chi_list_origin.index, y = chi_list_origin['chi'], mode = 'markers+lines+text',
    text = chi_list_origin['chi'].round(3), textposition = 'top right', textfont_size = 15))

fig.update_layout(
    {
        'title' : {'text':'Attribute-Cardio 별 Chi-Square 값', 'font':{'size' : 25}},
        'xaxis' : {'showticklabels':True, 'tickfont' : {'size' : 15}},
        'template' : 'plotly_white'
    })

fig.show() 


# 02. support / confidence / Null invariant method
# chi-square 계산(transaction dataframe 기준 : 각 attribute의 category)
# scipy.stats의 chi2_contingency를 통해서 contingency table 생성.
# contingency table을 바탕으로 chi-square와 p-value 계산.
chi_list = pd.DataFrame()
from scipy.stats import chi2_contingency
for i in range(len(transaction.columns)):
    f=transaction.columns[i]
    contigency = pd.crosstab(transaction[f],transaction['Cardio'])
    chi, p, dof, expected = chi2_contingency(contigency)
    chi_list = chi_list.append((pd.DataFrame({'chi' :chi, 'p-value':p}, index = [transaction.columns[i]+" & cardio"])))
    
# support 계산 함수
# transaction data와 item을 parameter로 받음
# item이 list 형태면 그대로 item을 반환하며, list가 아니면 list 형태로 바꿔서 items_list로 반환함 - sum()연산
# transaction data에서 item_list의 attribute를 받아 column기준 sum 연산 수행. 
# 변수 a : 위의 sum 연산결과가 items_list의 길이와 같은 row의 개수, 즉 해당하는 items_list의 요소를 모두 가지고 있는 row의 개수를 sum()
# 이를 전체 transaction 수(변수 b)로 나눠서 해당 item 집합이 발생한 확률을 구함.
def support(transaction, item): 
    items_list = item if isinstance(item,list) else list(item)
    a = np.sum(transaction.loc[:,items_list].sum(axis=1)==len(items_list)) 
    b = transaction.loc[:,items_list].shape[0]
    return a/b
  
# 위에서 만든 support 함수를 사용해서 집합 X, 집합 Y, 교집합의 support를 구해서 metric 공식에 대입.
# 얻은 결과값을 dataframe형태로 변환
Null_inv = pd.DataFrame()
for i in range(len(transaction.columns)):
    rslt01 = support(transaction, [transaction.columns[i]])
    rslt02 = support(transaction, ['Cardio'])
    rslt03 = support(transaction, (transaction.columns[i],'Cardio'))
    
    jacc = rslt03 / (rslt01+rslt02-rslt03)
    kulc = (0.5)*((rslt03/rslt01) + (rslt03/rslt02)) 
    ir = abs((rslt01 - rslt02)) / (rslt01+rslt02-rslt03)

    Null_inv = Null_inv.append((pd.DataFrame({'Jaccard' :jacc, 'kulczynski' :kulc, 'IR' : ir}, index = [transaction.columns[i]+" & cardio"]))
                               
# chi-square와 p-value, jaccard, kulczynski, IR을 하나의 데이터프레임으로 통합 - Null_inv
Null_inv = pd.merge(Null_inv, chi_list, how = 'outer', left_index=True, right_index=True)
Null_inv = Null_inv.drop(['Cardio & cardio', 'No_cardio & cardio'], axis = 0)
                               
# kulczynski를 기준으로 큰 순서부터 나열
Null_inv = Null_inv.sort_values('kulczynski', ascending = False)
Null_inv
                               
# Transaction Data의 Attribute-Cardio 별 Kulczynski / IR 값 시각화
fig = go.Figure()
fig.add_trace(
    go.Scatter(
    x = Null_inv.index, y = Null_inv['IR'], mode = 'markers+lines+text', name = 'IR'))

fig.add_trace(
    go.Scatter(
    x = Null_inv.index, y = Null_inv['kulczynski'], mode = 'markers+lines+text', name = 'Kulczynski'))

fig.update_layout(
    {
        'title' : {'text':'Attribute-Cardio 별 Kulczynski / IR 값', 'font':{'size' : 25}},
        'template' : 'plotly_white'
    })

fig.add_hline(y=0.5, line_dash="dot",
              line_color = "#ff0000",
              annotation_text="Kulczynski = 0.5", 
              annotation_position="bottom right",
              annotation_font_size=17,
              annotation_font_color="black"
             )

fig.show()
                               
## Null-Invariant Measures 결과
- kulczynski, IR, chi-square 값으로 몇가지 유추가 가능하다.
    - (1) 30 & cardio : kulczynski = 0.109444, IR = 0.980692, chi-square = 111.024261 이므로 둘의 관계는 negative하며, 두 집합의 분포가 inbalanced 하다.
    - (2) HBP_SYS & cardio : kulczynski = 0.640039, IR = 0.431196, chi-square = 10586.494635 이므로 둘의 관계는 positive하고, 두 집합의 분포 역시 어느정도 고르다.
- kulczynski의 결과가 0.5를 기준으로 나뉘고, 그에 따른 IR로부터 몇가지 결과를 얻을 수 있다. 
    - 이때 IR의 값이 하나의 categroy가 가지는 값에 대해서 다양하게 나오고 있으므로, 집합들 사이의 분포가 고르지 않은 경우가 많음을 알 수 있음.
    - 따라서 전체 데이터 크기에 대한 분포의 영향(e.x. BMI -> HIGH_OBESITY)을 배제할 수 없기 때문에 kulczynski와 IR 값만으로 attribute를 선택하는 것은 어려움.
    - kulczynski와 IR 값으로 선택한 attribute는 다음과 같음. 
    - [ap_hi, ap_lo, gluc, gender, active, age, cholesterol]
- 전체적으로 큰 chi-square값을 보이나, 그에 비해 작은 결과를 나타내는 attribute를 제외하면 남은 attribute는 아래와 같음.
    - [age, ap_hi, ap_lo, cholesterol, gluc, active, BMI] 
