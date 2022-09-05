---
title : "🧩 Data Mining (3) - QQ plot"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Distance, QQ plot]

toc : true
toc_sticky : true
use_math: true

date: 2022-06-30
last_modified_at: 2022-06-30
---  
* * *  
  
🧩 저번 포스팅에서는 우리가 다룰 data set에 대해 간략히 알아보았다. 이번에는 각 데이터의 상대적인 위치를 알 수 있는 몇가지 plot 방법에 대해 알아보자.  
  
## 1. Quantile plot  

- 각 object에 %를 부여함으로써 어느 <a>위치</a>에 존재하는지 알아내는 방법  
- Q<sub>1</sub> : 25%에 해당하는 object  
- Q<sub>2</sub> : <a>50%</a>에 해당하는 object    
- Q<sub>3</sub> : 75%에 해당하는 object  
  
- IQR : Q<sub>3</sub> - Q<sub>1</sub>  
    - <a>중간 50%</a>의 데이터가 존재하는 범위.  
    - IQR이 크면 중앙을 기준으로 데이터가 퍼져있음을 의미  
    - IQR이 작으면 중앙을 기준으로 데이터가 모여있음을 의미   
  
🧩 Function  
<center>$f_{i}=(i - 0.5)/N$</center>   

- 이때 i는 data의 인덱스이다.  
- ex1) 1 2 3 4 5 에 대해서 3의 f-value = (3-0.5) / 5 = 0.5 ▶ Q<sub>2</sub>  
- ex2) 1 2 3 4 5 6 에 대해서 3의 f-value = (3-0.5) / 6 = 0.42...  
- ex2에서 4의 f-value = (4-0.5) / 6 = 0.583...  
- 따라서 ex2에서 Q<sub>2</sub>는 3과 4 사이 어딘가에 존재한다.   
      
* * *  
## 2. Q-Q plot  
  
- Quantile plot을 사용해서 서로 다른 두 집단이 어떤 차이가 있는지 비교한다.  
- 두 집단의 Q<sub>1</sub>, Q<sub>2</sub>, Q<sub>3</sub> 값에 대한 실제 value값을 비교하여 두 집단의 전체적인 차이를 파악할 수 있다.  
  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176584168-c3b128f8-e81d-44bd-884f-32f45c59f65c.png" width="600" /></p>  
  
👉 model 1과 model 2를 좌표평면으로 옮긴 위의 Q-Q plot을 보면 같은 Q<sub>2</sub>에 대해서 각 모델이 서로 다른 값을 가지는 것을 볼 수 있다. 예를 들어, model 1과 model 2가 가격에 대한 데이터라면 model 2가 modle 1보다 비싼 가격이 좀 더 많을 거라고 생각할 수 있다.  
  
🧩 전체적인 개형을 한눈에 알아보고 대략적으로 비교하기에는 좋은 방법이지만, 세부적인 정보를 파악하기에는 그렇게 성능이 좋지는 않다.  
  
* * * 
## 3. Scatter plot  
  
- 산점도. 두 attribute 간의 관계 파악.  
  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176585863-983a352d-b726-4901-9445-7bae2b191469.png" width="600" /></p>  
  
👉 위 그래프들의 x축과 y축을 보면 알겠지만, 각 object들의 두 attribute 데이터를 해당하는 좌표에 흩뿌려서 관계를 알아낸다. 따라서 뿌려둔 점들의 대략적인 경향을 보면 두 attribute가 어떤 관계를 가지고 있을지를 짐작할 수도 있다.  
  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176586311-234b6ba8-60a0-4dec-afe7-ff7a957f9061.png" width="600" /></p>  
  
👉 위의 두 scatter plot에서 왼쪽이 positive하게 correlated되었다고 할 수 있을 것이며, 반대로 오른쪽은 negative한 관계가 있다고 할 수 있을 것이다. 하지만 항상 이렇게 눈에 띄는 연관관계가 있는 것은 아닌데, 이는 아래 plot에 나타냈다.  
  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/176586583-44e80cbc-7656-4e91-bf38-c7cdec1d97cd.png" width="600" /></p>   
  
🧩 scatter plot의 결과 두 attribute가 서로 어떤 관계를 가지는 경우도 있지만, 별 관계가 없는 경우 역시 살펴봤다. 어느 정도 예측할 수 있겠지만, 눈에 띄는 연관관계나 선형관계를 보여주는 경우는 거의 없다. 그래서 이와 관련된 여러가지 metric이 만들어진 것이다. 이와 관련해서는 Data preprocessing에서 다룰 예정이다.  
  
* * *  
🧩 이렇게 해서 QQ plot과 scatter plot까지 다뤄보았다. Quantile plot을 좀 더 자세히 살펴보기 위해서는 통계학적인 방법을 고려해줘야 하지만, 데이터마이닝을 공부하는 지금은 개념과 사용법을 아는 것이 더 중요하다고 생각해서 깊게 다루지는 않았다. 일단 전체적으로 한번 보고 나서, 세부적인 부분을 잡아나갈 때 다뤄보도록 하겠다😊.  
  
🧩 저번 포스팅과 이번 포스팅을 통해 데이터마이닝을 하기 위한 기초를 1/3 정도는 배운 것 같다. 다음 포스팅부터는 마지막 2/3을 채우기 위한 Distance measure를 배워보자🏃‍♂️🏃‍♂️.  
  
* * *
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
