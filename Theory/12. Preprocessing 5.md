---
title : "🧩 Data Mining (12) - Preprocessing_5 : Data Reduction - Linear Regression"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Preprocessing, Reduction, Linear]

toc : true
toc_sticky : true 
use_math : true  

date: 2022-07-11
last_modified_at: 2022-07-11 
---  

* * *  

🧩 [저번 포스팅](https://nyamin9.github.io/data_mining/Data-Mining-Preprocessing-4/)을 통해 데이터의 dimension을 줄이는 Data Reduction의 종류에 대해 알아보았다. 이번에는 object를 줄이는 방법 중 하나인 <b><a>Linear Regression</a></b>에 대해서 알아보도록 하자.  

* * *  

## 1. Parametric Data Reduction : Regression Analysis  

🧩 데이터의 object를 줄이는 Numerosity Reduction에는 파라미터를 사용하는 방법과 사용하지 않는 방법이 있다. 오늘 알아볼 Linear Regression은 파라미터를 사용하는 방법이기 때문에 <a><b>Parametric Method</b></a>가 무엇인가부터 간단히 보도록 하자.<br>  

🧩 그림을 보면 이해가 편할 것 같아서 그림을 하나 그려보았다.  
<p align="center"><img src="https://user-images.githubusercontent.com/65170165/178194905-e7b396c3-2b42-4696-9008-06766810128e.png" width="600" /></p>  

👉 위의 그림에서 우리의 데이터가 어떤 linaer 한 관계를 가지고 있을 거라고 가정하고, 그 모델을 $y=ax+b$라고 둔다. 그러면 그 모델에 $x_1$이라는 독립변수를 대입하여 $\hat{y}_1$이라는 예측값을 구할 수 있다. 이후에는 종속변수 $x_1$에 대해 해당 데이터의 원래 값인 $y_1$와 예측값 사이의 Error를 줄여나가는 방향으로 우리의 parameter를 업데이트하며 모델을 결정한다. 그리고 이 Error를 계산하는 방법에는 assumption model에 따라 여러가지 방법이 있다.  

* * *  

## 2. Linear Regression  

🧩 위와 같은 방식으로 데이터 설명을 위한 최적의 모델을 찾아나가는데, 이때 사용되는 가정의 종류에 따라서 그 모델의 형태가 달라진다는 것을 쉽게 예측할 수 있을 것이다. 그리고 사용하는 모델의 형태가 위에서 든 예시처럼 선형적인 형태를 가지고 있다면, 우리는 이 예측 모델을 <a><b>Linear Regression Model</b></a>이라고 부른다. 즉, <a>독립변수 $x$와 종속변수 $y$ 사이에 선형적인 관계가 있다</a>는 assumption 하에서 데이터를 설명하는 것이다. 그렇다면 한 번 알아보도록 하자.<br>  

- assumption model : $Y=WX+b\;\;(y = \hat{β}_1x+\hat{β}_0)$<br>  
- 직선으로 표현되는 모델  
- Parameter : $W,\;\,b\;\;(\hat{β}_1,\;\hat{β}_0)$
- Error Method : $Least-Squared\;Method\;(LSM)$<br>  

👉 이름은 어려워 보이지만 동작하는 알고리즘은 위에서 말한 기본적인 원리를 벗어나지 않는다. 가정에 의한 모델을 하나 만들고, 그에 대한 예측값을 구해 실제 값과의 Error를 계산한 뒤 오차를 최소화할수 있도록 파라미터를 업데이트하면 끝이다. 다만 여기서 유의할 점은 처음에 모델을 가정할 때 어느 정도는 데이터의 전체적인 개형과 비슷해야한다는 점과 Error를 계산하는 Method의 적절한 선택이 있을 것이다. 위에서 봤듯이 Linear Regression에서는 주로 LSM 을 사용할 텐데, 이제는 이에 대해 알아보도록 하자.<br>  

⭐ <b><a>$Least\;Squared\;Method : Residual\;Sum\;of\;Squares\;(RSS)$</a></b><br>  
<center>$for\;\;y = \hat{β}_1x+\hat{β}_0,$</center><br>  
<center>$RSS=E_1^2 + E_2^2+...+E_{n}^2\;=(y_1-(\hat{β}_1x_1+\hat{β}_0))^2+(y_2-(\hat{β}_1x_2+\hat{β}_0))^2+...+(y_n-(\hat{β}_1x_n+\hat{β}_0))^2$</center><br>  

위의 식을 천천히 살펴보면 알겠지만, 각 실제값과 예측값의 Error의 제곱의 합으로 model에 대한 전체 Error가 구해진다.  

최종적으로 이 Error를 최소화하는 파라미터를 찾아야 하는데, 그때 사용하는 방법은 아래와 같다.<br>  


⭐ <b><a>$Least\;Square\;Approach:\;Minimize\;RSS$</a></b><br>    
<center>$\hat{β}_1=\frac{\sum{(x_i-\overline{x})(y_i-\overline{y})}}{\sum{(x_i-\overline{x})^2}}$</center><br>  

<center>$\hat{β}_0=\overline{y}-\hat{β}_1\overline{x}$</center><br>  

위의 수식에서 $\overline{x}$와 $\overline{y}$는 각각 독립변수와 종속변수의 평균을 의미한다. 즉 예측값에서 원래 데이터에 대한 정보를 빼는 연산을 바탕으로 파라미터를 업데이트한다. 식은 복잡하지만, 그 의미와 연산 과정은 정말 간단한 원리로 구성되어 있는 것을 확인할 수 있다. 하지만 사람이 빅데이터에 대해서 저 연산을 하기에는 양이 너무 많기 때문에, 우리는 머신을 통해서 이 과정들을 수행할 수 있다. Linear Regression은 블로그에 더 자세하게 올려두었으니 아래 링크를 참고하면 좋을 것 같다👍👍.  

📝 [머신러닝 - Linear Regression 포스팅 모음](https://nyamin9.github.io/categories/machinelearning)  


* * *  

🧩 Linear Regression을 들어본 적이 있다면 아마 대부분 머신러닝에서 그 이름을 들어봤을 것이다. 하지만 앞서 대부분의 포스팅에서 볼 수 있듯이 데이터마이닝은 통계학이나 머신러닝 등 다양한 분야와 관련이 있는 학문이다. 그래서 하나를 알면 다른 하나도 이해하고, 또 다른 하나도 이해할 수 있는 그야말로 꼬꼬무하다는 느낌이 들었다. 그만큼 양이 많고 범위가 넓지만, 차근차근 따라가면 이해가 어려운 학문은 아니라고 생각한다🙃.  

🧩 다음 포스팅에서는 object를 줄이는 방법 중 두번째인 Nonparametric Method에 대해 알아보도록 하자🏃‍♂️🏃‍♂️.  
* * *  

<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div> 
