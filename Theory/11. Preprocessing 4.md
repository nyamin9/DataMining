---
title : "🧩 Data Mining (11) - Preprocessing_4 : Data Reduction - Introduce"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Preprocessing, Reduction]

toc : true
toc_sticky : true 
use_math : true  

date: 2022-07-09
last_modified_at: 2022-07-09 
---  

* * *  

🧩 저번 포스팅까지 해서 Data Integration을 다뤘다. 이제부터는 데이터 전처리를 위해 가장 중요하다고 할 수 있는 Data Reduction에 대해 알아보도록 하자.  

🧩 이번 포스팅에서는 Data Reduction을 왜 해야 하는지, 왜 중요한지. 그리고 어떤 종류가 있는지를 가볍게 다룰 것이다.  
* * *  

## 1. Data Reduction이란??  

🧩 실제로 우리가 다룰 데이터에는 <a>불필요한 정보</a>들도 많이 포함되어 있고, 이미 가지고 있는 값을 <a>중복</a>해서 가지고 있는 경우도 있다. 또한 비슷한 의미를 가지고 있어 합칠 수 있으나 원본 데이터에서는 여러 개의 attribute로 <a>나눠져</a> 있는 경우도 역시 존재한다. 이렇게 복잡한 데이터를 분석하는 데에는 시간도, 노력도 많이 필요하기 때문에 미리 데이터를 어느정도 간단히 만드는 과정이 필요하다. <b>이렇게 불필요한 attribute 또는 object를 줄여 데이터의 dimension을 줄이는 과정을 Data Reduction이라고 한다.</b>  

* * *  

## 2. Data Reduction 방법  

🧩 Data의 복잡도를 줄이는 방법에는 object를 줄이거나 attribute, 즉 dimension을 줄이는 방법이 존재한다. 또한 데이터를 그냥 압축하는 방법도 있다. 각각에 대해 간단히 알아보도록 하자.  

📝 <b>1. object 줄이기 : Numerosity Reduction</b><br>  
    - <a>Parametric Methods</a>  
        - 업데이트 할 parameter를 가지는 방법  
        - Reduction을 위한 Assumption이 필요함  
        - 즉, 데이터가 어떠한 모델에 fitting될 것이라는 임의의 모델을 가정하고 진행  
        - ex) Linear Regeression<br>    
    - <a>Non-Parametric Methods</a>  
        - parameter가 없는 방법  
        - assumption이 없음  
        - 모델을 가정하지 않기 때문에 어려움  
        - ex) Histogram, Clustering, Sampling<br>  

📝 <b>2. Attribute 줄이기 : Dimensionality Reduction</b><br>  
    - <a>Principal Component Analysis (PCA)</a>  
        - attribute를 combination한 새로운 dimension 생성  
        - 새로운 dimension을 축으로 해서 기존의 데이터를 설명하는 방법<br>  
    - <a>Subset Selection</a>  
        - 데이터를 가장 잘 설명할 수 있는 subset model을 선택해서 dimension을 줄이는 방법<br>  


📝 <b>3. Data Compression</b><br>  
    - <a>String Compression</a><br>  
    - <a>Audio / Video Compression</a><br>  

* * *   

🧩 이렇게 해서 간단하게 <a><b>Data Reduction</b></a>을 알아보았다. 다음 포스팅의 Parametric Method부터 본격적으로 알아보도록 하자🏃‍♂️🏃‍♂️.  

* * *  

<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>

