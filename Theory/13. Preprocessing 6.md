---
title : "🧩 Data Mining (13) - Preprocessing_6 : Data Reduction - Nonlinear Regression"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Preprocessing, Reduction, Nonlinear]

toc : true
toc_sticky : true 
use_math : true  

date: 2022-07-13
last_modified_at: 2022-07-13 
---  
  
* * *  

🧩 저번 포스팅에서는 Linear Regression에 대해 배워보았다. 이번에는 Parametric Reduction의 다른 방법인 Nonlinear Regression에 대해 알아보도록 하자.  

* * *  
## 1. Nonlinear Regression 이란??  

🧩 우리가 이미 알고 있듯이, <a>Parametric Reduction</a> 에는 linear regression과 nonlinear regression 이 있다. 이때 Linear Regression은 우리의 데이터가 선형적인 관계를 가지고 있을 것이라는 assumption 하에서 reduction이 진행된다. 반면에 오늘 살펴볼 <a><b>Nonlinear Regression</b></a>은 데이터가 비선형적인 관계를 가지는 경우를 가정한다. 이러한 차이만 알고 있으면 뒤에 이어질 내용을 이해하는 데에는 어려움이 없을 것 같다.<br>  
 
📝 <b>Nonlinear Regression</b><br>  
    - <a>비선형</a>으로 표현되는 모델을 가정  
    - parameter를 <a>두 개 이상</a> 사용함으로써 데이터를 설명할 수 있는 경우의 수가 증가함  
    - 하지만 데이터를 세세히 설명하는 모델이기 때문에 <a>overfitting</a> (과적합)이 발생할 수 있음  
    - overfitting에 의해서 <a>다른 데이터</a>에 적용했을 때의 예측력은 낮은 경우가 있음  
    - <a>다항식</a>의 형태로 모델이 표현됨 : polynominal regression  

👉 위에서 몇 가지 특징을 알아보았다. 요약하자면 많은 파라미터를 통해서 비선형적인 데이터도 잘 표현할 수 있도록 하는 모델이라는 뜻이다. 이제 모델의 형태를 살펴보자.<br>  

<center>$y = \hat{β_n}x^n + \hat{β_{n-1}}x^{n-1} + ... + \hat{β_2}x^2 + \hat{β_1}x + \hat{β_0}$</center><br>  

위와 같이 여러 항들을 통해서 데이터의 비선형성까지도 전반적인 표현이 가능하다. 하지만 가지고 있는 데이터를 잘 표현한다고 해서 모델의 항의 개수를 지나치게 늘려버린다면, 위에서 언급했듯이 overfitting이 발생할 수 있다. 이렇게 되면 다른 데이터에 대한 예측력이 낮을 수 밖에 없기 때문에 유용한 모델을 만드는 것이 불가능하다. 따라서 이를 잘 조절해서 모델을 생성하는 것이 중요하다고 할 수 있다.  

👉 기본적인 개념은 배웠으니, 이제 Nonlinear Regression의 종류를 알아보도록 하자🙃.  

* * *  

## 2. Nonlinear Regression 종류  

- <b>1. Multiple Regression</b><br>  
    - 일반적으로는 하나의 attribute에 대해서 regression을 한 후에 각각의 결과를 바탕으로 비슷한 예측값을 가지는 모델끼리 합치거나 연관관계가 높은 모델끼리 합치는 방식을 통해 reduction을 진행함  
    - 하지만 multiple regression은 각각을 regression 하기보다는 y라는 예측값을 여러 종류의 attribute를 선형함수로 취급함으로써 모델링한다.  
    - 즉, 데이터의 비선형성을 표현할 수 있다.  
    - 모델의 형태는 아래와 같다.<br>  

<center>$y=w_1x_1+w_2x_2+w_3x_3+...+w_nx_n+b$</center><br>  

👉 그리고 이 경우 모델의 error는 아래와 같이 계산된다. 당연히 이 Error를 최소화하는 방향으로 파라미터의 업데이트가 일어난다.<br>  


<center>$RSS=e_1^2+e_2^2+...+e_n^2=\sum(y_i-(\hat{β_0}+\hat{β_1}x_{i1}+\hat{β_2}x_{i2}+...+\hat{β_n}x_{in}))^2$</center><br>  

- <b>2. Log-linear Model</b><br>  
    - 데이터를 로그 스케일로 표현하는 것을 의미한다.  
    - 원래 데이터의 경우에는 지나치게 큰 값이 있으면 상대적으로 작은 값은 표현이 되지 않는 경우가 많으나, 로그 스케일을 사용하면 전반적인 데이터의 스케일이 줄어들어 attribute간의 관계를 찾기가 쉬워진다.  
    - 이를 통해 대소관계와 연관관계를 파악하여 data reduction을 수행한다.<br>  

* * *  

🧩 이렇게 해서 Parametric Data Reduction을 모두 알아보았다. 머신러닝에서는 가장 기본적으로 다루는 내용이고, 간단한 수학 지식만으로도 모델의 형태와 그 알고리즘을 이해하기 어렵지 않은 개념들이기 때문에 그렇게 엄청 자세하게 다루지는 않았다. 하지만 이런 방법을 통해 값을 예측하는 것 뿐만 아니라 데이터의 차원을 줄일 수 있다는 아이디어를 알면 좋을 것 같다😃😃.  

🧩 다음 포스팅에서는 Numerosity Reduction의 다른 종류인 <a>Nonparametric Data Reduction</a>에 대해서 알아보도록 하자🏃‍♂️🏃‍♂️.  

* * *  
    
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
