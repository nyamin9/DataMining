---
title : "🧩 Data Mining (5) - Distance_2 : Categorical / Binary"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Distance, Binary, contingency table]

toc : true
toc_sticky : true
use_math : true

date: 2022-07-02
last_modified_at: 2022-07-02
---  
* * *  
  
🧩 저번 포스팅을 통해서 object들 간의 Distance를 나타내는 Matrix를 만드는 법에 대해 알아보았다. 이제는 본격적으로 Distance measure에 대해 알아볼텐데, 이 measure들은 feature의 자료형에 따라 다르게 적용된다. 먼저 <a>categorical feature</a>와 <a>binary feature</a>에 대한 measure에 대해 알아보도록 하자.  
  
* * *  
## 1. Categorical Attributes - Nominal  
  
- <b>Simple Matching</b>  
    - 먼저 알아볼 방법은 simple matching이라는 방법이다. 이 방법을 통한 object 사이의 distance는 아래와 같이 표현된다.  
    <center>$d(i,j)=\frac{(p-m)}{p}$</center><br>  
    
    - 이때 $m$은 feature에 대해 같은 값의 개수이고, $p$는 전체 개수를 의미한다.  
    - 사실 위의 수식만 보고 이해하기가 쉽지 않기 때문에, 예를 한번 보도록 하자.    
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176986208-14de889e-3996-4c85-aeeb-b8783d5f1784.png" width="350" /></p>  

위에서 student 2와 3은 Blood Type은 같지만 Hair Color가 다르기 때문에  distance는 아래와 같다.  

<center>$d(s2,s3)=\frac{(2-1)}{2}=\frac{1}{2}$</center><br>  


반면 student 2와 student 4는 두 feature가 모두 다르기 때문에 distacne는  다음과 같다.  

<center>$d(s2,s4)=\frac{(2-0)}{2}=1$</center><br>  


이렇게 하면 간단하게 simple matching 을 통해 distance를 구할 수 있다.  

      
- <b>Use a large number of binary attributes</b>  
    - 각 nominal state에 대해 새로운 binary attribute를 생성하는 방법이다. 즉, categorical 형태로 주어진 각 feature들을 binary 형태로 바꿔주겠다는 의미이다. 이를 위 예시의 student 1과 student 2에 적용하면 아래와 같이 바뀐다. Blodd type A를 0으로, B를 1로 바꿔줬으며, Hair Color Black을 1로, Brown을 0으로 바꿔 나타내었다.  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176986217-f579dbbb-adf8-440a-a0db-2f6fdaca02b7.png" width="350" /></p>  

👉 그 후에 distance를 구하는 방법은 simple matching과 같다.  

<center>$d(i,j)=\frac{(p-m)}{p}$</center><br>  


* * *  


## 2. Categorical Attributes - Ordinal  

위에서 다룬 nominal data와는 다르게 순위가 있는 자료형이다.  

🧩 이 데이터의 distance를 구하는 방법은 ordinal variables를 그것의 순위로 변경해주는 것인데, 이는 아래와 같은 방식으로 정해진다.  

<center>$feature\;f,\;index\;\,i,\;\;r_{if}∈{1,2,...,M_{if}}\;\;and\;\;r_{if}=\;value\;ranking,\;M_{if}=\;amount$</center><br> 


<center>$Z_{if}=\frac{r_{if}-1}{M_{if}-1}$</center><br>  





👉 수식만 보면 뭔가 복잡해보이는데, 그냥 단순히 순위를 매긴다고 생각하면 편할 것 같다. 예시를 한번 살펴보도록 하자.  
  
freshman 1 / sopomore 2 / junior 3 / senior 4 에 대해서 각각의 $Z$값을 먼저 보면,  
$Z_{if}=0\;\;/\;\;\frac{1}{3}\;\;/\;\;\frac{2}{3}\;\;/\;\;1$ 로 계산이 된다.  

이 $Z$값을 바탕으로 해서 distance를 구하게 되는데, 그 계산은 단순 뺼셈 연산이다.  

<center>$d(freshman,senior) = 1-0=1$</center><br>  

<center>$d(junior,senior) = 1-\frac{2}{3}=\frac{1}{3}$</center>
  
* * *  
  
  
## 3. Binary Attributes - 0/1  
  
- binary attribute들은 0또는 1의 값을 가지기 때문에, 이를 간단하게 합쳐서 하나의 table로 만들 수 있다. 이 table을 <b><a>Contingency Table</a></b>이라고 하는데, 그 모습은 아래와 같이 나타난다.  
  
📝 <b>Contingency Table</b>  
  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176982654-de3d2fe3-5240-422e-9faf-9da222173bc6.png" width="600" /></p>  

👉 두 object가 모두 1인 경우에는 q, 모두 0이면 t, (i,j) = (1,0) 이면 s, (0,1) 이면 r로 각각 그 값이 집계된다.예측할 수 있겠지만, distance를 구할때는 주로 s와 r을, similarity를 구할 때는 q와 t를 사용한다.  

  
⭐⭐ contingency table에 있어서 반드시 고려해야 할 점이 하나 있다. 우리가 binary로 나타내는 데이터는 두 가지 경우로 명확히 나눠져야 한다. 하지만 이러한 경우가 그렇게 많이 존재하지는 않는데, 주로 나타나는 도메인이 질병의 양성 / 음성을 판단하는 도메인이다. 예를 들면 코로나 검사 결과가 양성(1)이냐 음성(0)이냐를 다루는 경우라 할 수 있겠다. 그리고 질병 관련 조사에서 우리가 관심있는 대상은 양성인 경우이지, 음성인 경우일 가능성은 그렇게 크지 않다. 하지만 두 조사 대상이 모두 양성인 경우(q)보다는 당연히 음성(t)일 가능성이 높기에, 위의 contingency table에서 q보다 t가 월등히 큰 값을 가질 것이다. 이렇게 asymmetric한 table에 대해서는 당연히 이 경우를 고려해야 한다⭐⭐.  
  
👉 이제 각각의 경우에 대한 distance를 구해보도록 하자.  

🧩 Distance measure for <a>symmetric</a> binary variables  
<center>$d(i,j)=\frac{r+s}{q+r+s+t}$</center><br>

  
🧩⭐Distance measure for <a>asymmetric</a> binary variables⭐  
<center>$d(i,j)=\frac{r+s}{q+r+s}$</center><br>

  
🧩⭐Similarity measure for <a>asymmetric</a> binary variables⭐  
<center>$Jaccard\;\,coefficient=Sim_{jaccard}(i,j)=\frac{q}{q+r+s}$</center><br>
  
🧩 예시를 한번 살펴보도록 하자!!  


<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176986240-c0f486c9-e7d3-4625-abad-3849d8602d60.png" width="600" /></p>  
  
👉 어떤 질병에 관련된 7개의 feature를 가진 3개의 object로 구성된 데이터임을 확인할 수 있다. 이때 gender는 symmetric한 특징을 가지고 있기 때문에 이는 제외하고 distance를 계산해 줄 것이다. 또한 test의 결과에서 나오는 P는 1로, N은 0으로 긴주한다. 이를 바탕으로 contingency table을 만들면 아래와 같다.  
  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176984067-0e80896d-d1c4-45bf-ba7c-7315fcdec53c.png" width="600" /></p>  
  
🧩 위의 공식에 따라서 distance를 구해보자.  

<center>$d(i,j)=\frac{r+s}{q+r+s}$</center><br>  
<center>$d(jack,jim)=\frac{1+1}{1+1+1}=0.67$</center><br>  
<center>$d(jack,mary)=\frac{0+1}{2+0+1}=0.33$</center><br>  
<center>$d(jim,mary)=\frac{1+2}{1+1+2}=0.75$</center><br>



🧩 이렇게 해서 binary data에 대한 distance measure 역시 다뤄봤다. 고려해야 할 것도 있고, 그 경우마다 적용되는 공식도 살짝씩 달라지지만 서로 다른 것들로 distance를 계산하고 같은 것으로 similarity를 게산한다는 것만 생각하면 그렇게 어려운 개념은 아닐 것 같다.  
  
* * *  
🧩 이번 포스팅에서는 categorical data에 대한 distance measure를 알아보았다. 종류가 다양하고, 데이터의 도메인에 따라서 적용하는 법이 다르지만 위의 예시들만 잘 살펴봐도 나름 스근하게 넘어갈 수 있는 내용들인 것 같다😊. 앞으로 나올 내용들의 기초가 되는 부분들이기 때문에 나름 자세히 다뤄보었는데, 충분한 설명이 되었으면 좋겠다. 이제 다음 포스팅에서는 Numerical Data의 distance를 구해보도록 하자🏃‍♂️🏃‍♂️.  
  
  
* * *  
  
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
