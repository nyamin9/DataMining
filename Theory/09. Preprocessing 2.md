---
title : "🧩 Data Mining (9) - Preprocessing_2 : Data Integration - chi-square test"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Preprocessing, Integration]

toc : true
toc_sticky : true 
use_math : true  

date: 2022-07-06
last_modified_at: 2022-07-06 
---  

* * *  

🧩 저번 포스팅에서 Data Cleaning에 대해서 간단하게 알아보았다. 이제는 본격적인 전처리를 위한 방법들을 배워나갈 것인데, 먼저 categorical data의 integration을 위한 <b><a>chi-square test</a></b>를 알아보도록 하자.  
* * *  

## 1. Data Integration  

🧩 먼저 Data Interation이 무엇인지, 왜 하는지 짚어보자.  

🧩 Data Integration은 여러 출처의 데이터를 일관된 저장소로 통합하거나 데이터베이스를 통합하여 각각의 데이터를 보다 축소된 범위에서 한번에 다루기 위한 방법이다. 이는 기업이나 큰 데이터베이스에서 주로 사용되는 개념이고, 보통 Data Integration이라면 데이터의 attribute를 통합하여 복잡할 수 있는 연산을 줄이거나 데이터의 dimension을 줄여 분석하는 것에 의미를 둔다.  

👉 즉, 앞으로 우리가 배워나갈 여러가지 measure들은 attribute들의 Integration을 위한 기준을 정하는 것이라 이해하면 될 듯 하다.  

* * *  

## 2. Categorical Data : chi-square test  

🧩 Data Integration의 정의도 알았으니 이제 첫번째 measure를 알아보도록 하자. 첫번째 방법은 범주형 데이터의 통합을 위한 <b><a>chi-square test</a></b><a> ($χ^2-test$)</a> 이다.<br>  

🧩 카이제곱검정을 통해 attirubute<sub>i</sub>와 attribute<sub>j</sub>에 대해서 두 feature 간의 correlation(연관성)이 있는가 알아보기 위해서는 한 가지 가설이 필요하다. 이를 우리는 <b><a>Null 가설</a></b>이라고 부를 것이다.<br>  

⭐ Null hypothesis : 두 attribute i, j가 서로 독립이다. 즉, 서로 아무런 연관성이 없다.  

👉 이제 카이제곱검정을 위한 준비를 모두 끝냈다. 본격적으로 알아보자.<br>  


📝 <b>$χ^{2}-test$</b>  

<p align="center"><img src="https://user-images.githubusercontent.com/65170165/177462175-b46d34c0-ce0c-40af-9782-96a446327ec4.png" width="600" /></p>  

<center>👉 각 attribute A와 B가 i, j의 case를 가질때 통계값은 다음과 같이 구해진다.</center><br>  

<center>$e_{ij} = \frac{count(A=a_i)\times{count(B=b_j)}}{n}\;\,,$</center><br>

<center>$χ^{2} = \sum_{i=1}^c\sum_{j=1}^r\frac{(o_{ij}-e_{ij})^2}{e_{ij}}$</center><br>  

⭐ $e_{ij}$를 구할 때 Null 가설이 적용된다. 즉, $e_{ij}$는 두 attribute가 서로 독립이라는 가정 하에 구해지는 통계값이고, $o_{ij}$는 어떠한 가정 없이 표본의 조사 결과 구해지는 실제 값이다.  

⭐ 즉, $o_{ij}$ (실제 관측값)와 $e_{ij}$ (독립 가정에 의한 값)의 차이가 크다는 것은 실제 attribute i와 j가 서로 독립이 아니라는 것을 의미한다. <b>따라서 $χ^{2}$ 가 클수록 두 attribute간의 correlation이 크다.</b>  

🧩 $χ^{2}$ 의 연산식을 보면 알겠지만, 두 시그마의 위끝이 다르다. 즉, 각각의 attribute가 가지는 case의 수에 상관없이 chi-square 값을 계산할 수 있다는 의미이다. 따라서 활용도가 굉장히 좋은 방법 중 하나라고 할 수 있을 것 같다.  


👉 가볍게 에시를 한번 살펴보고 마무리하도록 하자.  

* * *  

## 3. 📝 chi-square test 예제  

🧩 어떤 정책에 성별 attribute A와 찬성 / 반대 case를 가지는 attribute B 간의 correlation을 chi-sqare test를 통해 구해보자.  

<p align="center"><img src="https://user-images.githubusercontent.com/65170165/177465101-e8e1367c-7458-4430-a94c-98176d9fe1e4.png" width="600" /></p>  

각 attribute를 정리한 값은 위의 표와 같다. 이를 바탕으로 각각의 $e_{ij}$를 구해보자.<br>  


<center>$e_{11} = \frac{M\times{Y}}{n} = \frac{450\times{300}}{1500}=90$</center><br>  
<center>$e_{21} = \frac{F\times{Y}}{n} = \frac{1050\times{300}}{1500}=210$</center><br>  
<center>$e_{12} = \frac{M\times{N}}{n} = \frac{450\times{1200}}{1500}=360$</center><br>  
<center>$e_{22} = \frac{F\times{N}}{n} = \frac{1200\times{1050}}{1500}=840$</center><br>  

이제 이 값들로 chi-square 값을 구해주면 된다. 보다 편한 이해를 위해서 $e_{ij}$를 표에 넣어 표현해주었다.  

<p align="center"><img src="https://user-images.githubusercontent.com/65170165/177466257-03c32f6a-a8c9-48d2-80b4-3101d6380ca4.png" width="600" /></p>  

마지막으로 chi-square값을 구해주자.  

<center>$χ^{2} = \frac{(250-90)^2}{90}+\frac{(200-360)^2}{360}+\frac{(50-210)^2}{210}+\frac{(1000-840)^2}{840}=507.93$</center><br>  

👉 이 정도면 정말 말도 안되게 큰 값이다. 즉, 독립이라는 가정 (Null hypothesis) 하에서느 절대로 나올 수 없는 값이므로, <b>두 attribute가 서로 높은 correlation을 가진다는 의미</b>라고 할 수 있을 것이다.  

* * *  

🧩 이렇게 수식도 배우고, 예제를 하나 다룸으로써 chi-square test를 알아보았다. 직접 하기에는 계산할 양이 적은 편은 아니고, attribute의 case가 늘어날수록 연산량이 늘어나겠지만, 우리의 주변에 있는 수많은 똑똑한 분들 덕분에 이를 컴퓨터에서 한번에 계산할 수 있는 라이브러리도 있고, 함수도 있다. 정말 멋지고 소중한 분들이다(넙죽🙇‍♂️🙇‍♂️).  


🧩 통계를 배운 분들이라면 아실 수 있겠지만, 통계에서의 카이제곱검정과 같은 의미를 가진다. 다만 통계에서는 유의수준과 p-value를 통해서 주로 검정을 수행하지만, 오늘 배운 내용에서는 $χ^{2}$ 값을 직접 구해서 그 크기로 correlation을 분석하다는 점이 살짝 다르다.  

🧩 이번 포스팅에서는 categorical data를 위한 measure를 알아보았다. 다음 포스팅에서는 Numerical Data를 위한 방법들을 알아보도록 하자😀.  

* * *  
  
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>  
