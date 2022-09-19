---
title : "🧩 Data Mining (8) - Preprocessing_1 : Data Cleaning"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Preprocessing, Cleaning]

toc : true
toc_sticky : true 
use_math : true  

date: 2022-07-05
last_modified_at: 2022-07-05 
---  
* * *  

🧩 이번 포스팅부터는 <b><a>Data Preprocessing</a></b>, 즉 데이터 전처리에 대해서 다룰 생각이다. 어쩌면 정확한 데이터 분석이나 마이닝을 위해서 가장 중요한 부분이라고도 할 수 있기 때문에, 이왕 하는 거 한번에 자세히 알아보도록 하자.  

🧩 Data Preprocessing은 아래와 같은 방법들로 구성된다.  
- Data Cleaning  
- Data Integration  
- Data Reduction / TRansformation  
- Dimensinality Reduction  

👉 Distance 처럼 전처리도 각 상황에 맞는 여러가지 measure들을 가지고 있다. 한번 천천히 알아보자😀.  

🧩 이번 포스팅에서는 첫번째 방법인 <b><a>Data Cleaning</a></b>을 다룰 것이다.  

* * *
## 1. Data Cleaning 소개  

🧩 우리가 가지고 있는 데이터는 대부분 불필요한 부분을 가지고 있거나, 정확하지 않은 부분을 가지고 있는 데이터일 가능성이 높다.  이런 부분들을 만드는 원인들은 여러가지가 있는데, 이 중에서 대표적인 몇가지를 가져왔다.  

- <b>Incomplete</b> : 데이터들 사이에 <a>missing value</a> 존재  
- <b>Noisy</b>: 데이터 중간에 섞여있는 <a>noise, errors, outliers</a>  
- <b>Inconsistent</b> : 두 feature의 <a>불일치</a> - ex) age = 56, birth = 2020    
- <b>Intentional</b> : <a>일반화</a> - ex) 1월 1일은 모든 사람들의 생일이다.  

따라서 이 부분들을 적절히 처리해서 데이터를 깨끗이 만들어줘야 한다. 대표적으로 발생하는 앞의 두가지 경우를 위주로 살펴보자.  

* * *
## 2. Incomplete (Missing) Data  

- 몇몇 attribute에서 value가 없는 데이터를 의미한다.  
- 이러한 missing value가 나타나는 원인은 다음과 같다.  
    - 측정 장비의 오작동  
    - 기록된 다른 자료와의 불일치에 의한 삭제  
    - 오해로 인한 데이터 미입력  
    - 특정 데이터가 입력 시에 불필요하다고 생각되는 경우<br>  

- 이러한 데이터들은 빈 자리에 임의의 값을 채워넣어 처리해줄 수 있다. 이때 채워넣는 값들은 아래의 방법을 기준으로 정해진다.<br>  


- <b>처리 방법</b>  
    - 해당 튜플(object) <a>무시</a> : 보통 class의 label이 존재하지 않는 튜플인 경우 무시한다.  
    - 빈 value를 <a>수동으로 일일이 입력</a> : 작업량이 너무 많고, 사실상 불가능하다.  
    - 빈 value에 <a>자동으로 입력</a>  
        - global constanct : 임의의 숫자 / 문자 입력 ex) 1, 0, 'NaN'...  
        - attribute mean : attribute의 평균 입력  
        - attribute mean - same class : 같은 class를 가진 object의 평균 입력  
        - Bayesian formula or Decision Tree : inference 기반 - prediction 입력  

* * *  
## 3. Noisy Data  

- 데이터에서 <a>Noise</a>는 다음과 같이 정의된다.  
    - 측정된 변수의 random error / variance  
    - Duplicated records(중복기록)  
    - Incomplete / Inconsistent<br>  

- <b>처리방법</b>  
    - <a>Binning</a> : 정렬되어 있는 데이터에 대해 같은 사이즈의 bins로 나눔(equal-frequency)  
        - smooth by bin means / median / boundaries  
    - <a>Regression</a> : 가지고 있는 데이터를 바탕으로 noise를 fitting해서 noise 보정  
        - smooth by fitting the data into regression functions  
    - <a>Clustering</a> : outlier 발견 / 제거  
    - Semi-Supervised : 컴퓨터 + 사람의 noise 발견 / 처리  

🧩 각 처리 방법은 앞으로 좀 더 자세히 다룰 것이기 때문에 여기서는 간단히 개념만 짚어보았다.  


* * *  
## 4. Data Cleaning Process  

- <b>1. Data Discrepancy Detection : 데이터 불일치 발견</b>  
    - <a>Using Metadata</a> : 데이터에 대한 정보  
        - 데이터의 소속 domain, 데이터 범위, 데이터의 distribution  
    - <a>Checking Uniqueness Rule</a> : 데이터가 유일한가  
        - ex) 주민등록번호  
    - <a>Consecutive Rule</a> : 데이터가 연속적인가. 어색하지 않은가.  
    - <a>Null Rule</a> : 데이터에 null 값이 존재하는가.  
    - <a>Data Scrubbing</a> : 도메인에 대한 기본 지식을 바탕으로 오류검출 / 수정  
        - ex) 우편번호 / 철자검사  
    - <a>Data Auditing</a> : 데이터를 분석하여 규칙을 검출하고 오류를 검출  
        - ex) Clustering<br>  


- <b>2. Data Migration & Integration : 데이터 이동 / 통합</b>  
    - <a>Data Migration Tools</a> : 변환할 attribute 지정  
        - ex) sex $\rightarrow$ gender  
    - <a>ETL tools : Extraction / Transformation / Loading</a>  
        - 사용자 인터페이스(UI)를 통한 데이터 변환 지정<br>  

- <b>3. Integration of the two Process : 불일치 검출 / 변환</b>  
    - 반복적이고 상호적인 단계를 통해 두 데이터 간의 Integration 진행   

* * *  
🧩 이렇게 데이터 전처리의 첫 번째 단계인 Data Cleaning에 대해서 알아보았다. 간단하게 개념만을 다루었고 특정 예시를 들지 않았기 때문에 이것만 보고 바로 이해하는 것은 어렵다고 생각하지만, 그냥 이런 것들이 있구나~~ 정도만 알면 좋을 것 같다. 어차피 이번에 대략적으로 다룬 개념들을 앞으로 더 세부적으로 다룰테니, 천천히 함께 배워가도록 하자😊. 다음 포스팅부터는 Data Integration을 다룰 것이다🏃‍♂️🏃‍♂️.  

* * *  

<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
