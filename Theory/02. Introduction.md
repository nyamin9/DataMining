---
title : "🧩 Data Mining (2) - Introduction"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining]

toc : true
toc_sticky : true

date: 2022-06-29
last_modified_at: 2022-06-29
---  
* * *
  
🧩 데이터마이닝의 첫번째 포스팅이다. 이번 포스팅에서는 간단하게 데이터마이닝이 무엇인지 개념 위주로 살펴보고자 한다.  
  
* * *

## 1. 데이터 마이닝이란??
  
- <b>기존의 데이터에서 의미있는 <a>패턴</a>이나 <a>지식</a>을 얻는 것.</b>    

- 간단한 검색이나 정형화된 규칙을 기반으로 작업하는 것은 데이터마이닝이라고 보기 어렵다.  
  
* * *  
## 2. 데이터마이닝 순서
  
-  데이터 결정 : time-series / sequence / text / graphs / social...  
  
-  도출할 insight 결정 : classification / clustering / trend / deviation...  
  
-  적용 기술 결정 : machinelearning / deeplearning / statics / pattern...  
  
-  적용할 도메인 결정 : retail / banking / bio-data / stack / text...  
  
  - 데이터 타입에 맞는 방법을 사용해서 마이닝을 진행해야 한다.  
    
    
👉 Data Cleaning ▶ Data Integration ▶ Data Selection ▶ Data Transform ▶ Data Mining ▶ Pattern Evaluation ▶ Knowledge Presentation  
  
👉 각각의 순서에서 사용하는 기법들은 앞으로 포스팅할 예정이다!!  
  
* * *
## 3. 데이터마이닝의 Function
  
- 데이터마이닝 : 유의미한 패턴을 알아내는 것. 따라서 이를 위한 function들이 존재한다.  
  
- <b>Generalization</b>  
  - Information Integration & Data warehouse construction  
  - Data Cube  
  - 가지고 있는 정보들을 통해 다양한 각도로 데이터를 일반화.  
  - 대용량의 데이터를 다루는 경우에 주로 사용함.  
    
    
- <b>Pattern Discovery</b>  
  - 데이터 / Attribute 간의 관계와 패턴을 발견  
  - ex) Frequent Patterns / Correlation Analysis  
    
    
- <b>Classification</b>  
  - Supervised learning with <a>training data</a> (examples)  
  - 알려지지 않은 class를 예측하는 것 (<a>label</a>)  
  - support vector machine / deep learning / bayesian / decision tree / logistic regression...  
      
      
- <b>Clustering</b>  
  - Unsupervised learning  
  - class를 모르는 상태로 유사한 데이터끼리 군집화  
  - 묶고 봤더니 묶인 데이터들의 특징이 이러이러하더라를 판단  
  - rule : Maximizing intraclass similarity & Minimizing interclass similarity   
  👉 같은 그룹 내 유사성 최대화 & 다른 그룹끼리의 유사성 최소화  
      
      
- <b>Outlier Analysis</b>  
  - 데이터가 노이즈인지, 필연적으로 생긴 특이 케이스인지 구분  
  - fraud detection / rare events analysis  
      
      
- <b>Time & Ordering</b>  
  - 주식, 주가, 태풍처럼 주기적으로 발생하는 패턴 분석  
  - Sequential Pattern, 시간상 순서관계 고려  
  - 유전자 시퀀스 분석, 유사성 파악  
      
      
- <b>Structure & Network</b>  
  - 그래프 마이닝, 네트워크 분석, 웹 마이닝  
    
    
- <b>Major Issues</b>  
  - 효율적인 알고리즘인가  
  - 데이터 양이 증가했을 때도 잘 적용되는가  
  - 데이터의 형태에 따라 달라지는가  
  - 사회적으로 사용 가능한 데이터인가 ex) 프라이버시  
    
  
* * *  
  
🧩 이렇게 해서 간단하게 데이터마이닝이 뭔지, 우리가 신경써야 할 부분이 어디인지, 그리고 얼마나 다양한 상황에 사용될 수 있는지를 간략하게 알아보았다. 다음 포스팅에서는 데이터와 object 간의 유사성을 판단하기 위한 Distance measure에 대해 알아보도록 하자.  
* * *  
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
