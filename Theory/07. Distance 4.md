---
title : "🧩 Data Mining (7) - Distance_4 : Cosine 유사도"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Distance, Document, Cosine]

toc : true
toc_sticky : true
use_math : true

date: 2022-07-04
last_modified_at: 2022-07-04
---  
* * *  
  
🧩 Distance Measure 마지막 포스팅이다🙄. Document Frequency를 위한 Cosine Similarity에 대해 알아보자.  

## 1. Cosine Similarity of two vectors  

🧩 <a>Document Frequency</a>가 무엇인지 궁금할 수 있을 텐데, 신문기사나 인터넷 기사를 가장 대표적인 예시로 생각하면 될 것 같다. 연예기사에는 연예기사만의 자주 나오는 용어들이 있을 것이고, 스포츠 기사에는 그만의 자주 등장하는 용어들이 있을 것이다. 서로 다른 두 기사들 간의 similarity를 계산해서 유사서을 알아보는 것이 <b><a>Cosine Similarity</a></b>의 목적이다. 또한 단순히 텍스트들의 유사성 뿐만 아니라 유전체에 대한 분석도 진행할 수 있는 measure이기 때문에 Gene feature 혹은 biologic toxonomy등의 도메인에서도 사용하는 추세이다.  

🧩 예시부터 살펴보도록 하자.  

<p align="center"><img src="https://user-images.githubusercontent.com/65170165/177064371-4111bb08-8ad1-4639-a10d-46b8c7864b2a.png" width="600" /></p>  

👉 위의 예시에서 각각의 Document들이 신문기사를 의미하고, 각 column들이 신문기사에서 나오는 용어들의 빈도를 나타낸다. 이제 우리는 Frequency를 분석하기 위해서 각 document의 빈도를 vector로 표현할 것이다. 각각의 벡터는 아래와 같이 표현된다.   

<center>$\overrightarrow{d_{1}}=[5,0,3,0,2,0]$</center><br>  
<center>$\overrightarrow{d_{2}}=[3,0,2,0,1,1]$</center><br>  
<center>$\overrightarrow{d_{3}}=[0,7,0,2,1,0]$</center><br>  
<center>$\overrightarrow{d_{4}}=[0,1,0,0,1,2]$</center><br>  

앞으로 이 벡터들을 <a>term-frquency vector</a> 라고 부를 것이다. 이제 이 벡터들을 가지고 similarity를 구하기 위한 measure를 살펴보자.  

📝 <b>Cosine Measure</b>  

두 벡터 $\overrightarrow{d_{1}}$, $\overrightarrow{d_{2}}$에 대하여 (단, 두 벡터는 term-frquency vector)  

<center>$cos(\overrightarrow{d_{1}}, \overrightarrow{d_{2}}) = \frac{\overrightarrow{d_{1}}\cdot\overrightarrow{d_{2}}}{|\overrightarrow{d_{1}}|\times|\overrightarrow{d_{2}}|}$</center><br>  

👉 벡터도 나오고, 내적도 나와서 얼핏보면 복잡해보이는 식이긴 하지만 그냥 단순히 내적 계산 식에서 파생되는 measure이다. 내적값은 두 벡터의 크기의 곱에 두 벡터 사이의 각인 θ의 코사인 값을 구해 곱해주는 것이기 때문에, 그냥 그 식을 넘겨주는 것 뿐이다.  

👉 코사인 그래프를 생각해보면 코사인 값은 θ가 작을수록 커진다.  따라서 cosine similarity 깂인 $cos(\overrightarrow{d_{1}}, \overrightarrow{d_{2}})$ 가 커지면 두 벡터 사잇각인 θ가 작아서 두 벡터가 서로 가깝다는 것을 의미한다. 정리하면 다음과 같다.  

- $cos(\overrightarrow{d_{1}}, \overrightarrow{d_{2}})$가 크다 = 사잇각 θ가 작다 = <a>두 벡터가 서로 가깝다</a>  

- $cos(\overrightarrow{d_{1}}, \overrightarrow{d_{2}})$가 작다 = 사잇각 θ가 크다 = <a>두 벡터가 서로 멀다</a>  

🧩 위의 예시에서 직접 cosine similarity를 구해보는 것으로 끝내자😉.  

<center>$\overrightarrow{d_{1}}=[5,0,3,0,2,0]$</center><br>  
<center>$\overrightarrow{d_{2}}=[3,0,2,0,1,1]$</center><br>  
<center>$\overrightarrow{d_{3}}=[0,7,0,2,1,0]$</center><br>  
<center>$\overrightarrow{d_{4}}=[0,1,0,0,1,2]$</center><br>  

$cos(\overrightarrow{d_{1}}, \overrightarrow{d_{2}})$ 에 대해서  

$\overrightarrow{d_{1}}\cdot\overrightarrow{d_{2}} = 15+0+6+0+2+0=23$<br>  
$|\overrightarrow{d_{1}}| = \sqrt{25+0+9+0+4+0} = \sqrt{38}$<br>  
$|\overrightarrow{d_{2}}| = \sqrt{9+0+4+0+1+1} = \sqrt{15}$<br>  
$cos(\overrightarrow{d_{1}}, \overrightarrow{d_{2}})=\frac{23}{\sqrt{38}\times\sqrt{15}} = 0.963$<br>  

- cosine similarity 값이 1에 가까운 큰 값을 가지기 때문에 두 벡터는 서로 가깝다고 할 수 있다.  

* * *  

## 2. Distance Measure 요약  

- <a>Distance Matrix</a>  
- Q-Q plot  
- Scatter plot  
- <a>Categorical Attributes</a> : Simple Matching  
- <a>Binary Attributes</a> : contingency table  
- <a>Numeric Data</a> : Minkowski Distance  
    - Manhattan (1)  
    - Euclidean (2)  
    - Supremum (∞)  
- <a>Document / Term Frequency</a> : Cosine Similarity  

🧩 Distance Measure 관련 링크를 아래에 첨부해두었으니 필요한 사람은 참고하면 정리에 도움이 될 것 같다😉.  

* * *

[📝 1. QQ plot / Scatter plot 관련 포스팅](https://nyamin9.github.io/data_mining/DataMining-QQ-plot/)  
[📝 2. Distance Matrix 관련 포스팅](https://nyamin9.github.io/data_mining/Data-Mining-Distance-1/)  
[📝 3. Categorical / Binary Attributes 관련 포스팅](https://nyamin9.github.io/data_mining/Data-Mining-Distance-2/)  
[📝 4. Numeric Data - Minkowski Distance 관련 포스팅](https://nyamin9.github.io/data_mining/Data-Mining-Distance-3/)  

* * *  

🧩 이렇게 해서 Distance Measure를 모두 알아보았다. 수식이 복잡해보이는 경우도 있고, 그 개념이 헷갈리는 경우도 있지만 어떤 자료형의 데이터에 어떠한 measure를 사용하는지 알고 있으면 distance를 계산하는 데에는 전혀 어려움이 없을 것 같다. 대부분의 measure가 파이썬이나 R에 구현되어 있으니 말이다😀😀ㅎㅎ.  

🧩 다음 포스팅부터는 Data Preprocessing을 위한 방법들을 알아보자!!  

* * *  
  
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
