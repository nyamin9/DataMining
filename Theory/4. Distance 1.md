---
title : "🧩 Data Mining (4) - Distance_1 : Distance Matrix"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Distance]

toc : true
toc_sticky : true

date: 2022-07-01
last_modified_at: 2022-07-01
---  
* * *  
  
🧩 저번 포스팅들을 통해서 데이터들의 기본적인 특징들을 알아보았다. 이번 포스팅부터는 본격적으로 Distance measure에 대해 알아보도록 하자.  
  
## 1. Similarity / Dissimilarity
  
- <b>Similarity</b>  
    - 데이터들의 유사한 정도  
    - 범위 : [0,1]  
    - 0 : No Similarity  
    - 1 : Completely Similar  
  
- <b>Dissimilarity</b>  
    - 데이터들의 다른 정도 (= distance)  
    - 범위 : [0,1]  
    - 0 : No Distance  
    - 1 : Completely Dissimilar  
  
  
🧩 위의 두 친구들을 비교해보면 알겠지만 서로 정반대의 의미를 가진다. 두 개념 모두 같은 범위를 가지지만, 그 값이 의미하는 바는 정반대라고 이해하면 될 듯 하다. 이 두 개념을 먼저 다루는 이유는, 앞으로 설명할 내용들에서 계속해서 등장하기 때문이다.  
  
🧩 그리고 위의 두 개념들을 통합해서 <b><a>Proximity</a></b>라고 한다.
  
* * *  

## 2. Dissimilarity Matrix  
  
🧩 이번에는 두 object 들 사이의 Distance를 나타내는 Matrix인 <a>Dissimilarity Matrix</a>에 대해 알아보자. 보다 편한 이해를 위해 앞서서 설명한 Data Set의 구조를 좀 더 자세히 나타내줄 것이다. 그리고 앞으로는 이 구조를 <a>Data Matrix</a>라고 부르자.  




  
<b>📝Data Matrix</b>  

||feature 1|feature2|feature3|...|feature m|
|:---:|:------:|:--------:|:--------:|:---:|:---------:|
|<b>d 1</b>|x<sub>11</sub>|x<sub>12</sub>|x<sub>13</sub>|...|x<sub>1m</sub>|
|<b>d 2</b>|x<sub>21</sub>|x<sub>22</sub>|x<sub>23</sub>|...|x<sub>2m</sub>|
|...|...|...|...|...|...|
|<b>d n</b>|x<sub>n1</sub>|x<sub>n2</sub>|x<sub>n3</sub>|...|x<sub>nm</sub>|  


  
👉 위의 Data Matrix를 보면 알 수 있지만 위 구조는 m개의 feature로 표현되는 n개의 object로 이루어진다. 즉, (n x m) matrix이다.  
  
🧩 이제는 이를 바탕으로 해서 Dissimilarity Matrix를 만들 생각인데, 이를 위해서 우리는 비교하고 싶은 하나의 feature를 골라올 것이다. 그렇게 만들어지는 구조는 아래의 그림과 같다.  
  
  
  
<b>📝Dissimilarity Matrix</b>  

  
||d 1|d 2|d 3|...|d n|
|:---:|:------:|:--------:|:--------:|:---:|:---------:|
|<b>d 1</b>|d(1,1)|d(1,2)|d(1,3)|...|d(1,n)|
|<b>d 2</b>|d(2,1)|d(2,2)|d(2,3)|...|d(2,n)|
|<b>d 3</b>|d(3,1)|d(3,2)|d(3,3)|...|d(3,n)|
|...|...|...|...|...|...|
|<b>d n</b>|d(n,1)|d(n,2)|d(n,3)|...|d(n,n)|  



👉 각각의 d(i,j)는 하나의 feature에 대해 정해둔 Distance Measure를 통해 구한 objec i와 object j의 거리를 나타낸다. 이를 통합해서 Matrix 형태로 표현한다. 이때 자기 자신과의 distance는 당연히 0이고, d(1,2)와 d(2,1)은 서로 같은 object들 간의 비교이기 때문에 서로 같은 값을 가진다. 따라서, Symmetric(대칭성)에 의해 이 Matrix는 아래와 같이 표현되기도 한다.  




  
||d 1|d 2|d 3|...|d n|
|:---:|:------:|:--------:|:--------:|:---:|:---------:|
|<b>d 1</b>|0|||||
|<b>d 2</b>|d(2,1)|0||||
|<b>d 3</b>|d(3,1)|d(3,2)|0|||
|...|...|...|...|0||
|<b>d n</b>|d(n,1)|d(n,2)|d(n,3)|...|0|  


  
🧩 앞서 말했듯이 이 distance를 구하기 위한 measure를 미리 정해주는데, 이 measure들은 variables의 자료형에 따라 선택하는 기준이 달라진다. 이 내용들은 다음 포스팅에서 소개할 것이다.  
  
* * *  

🧩 이렇게 해서 앞으로 Distance들을 정리할 Matrix의 생성까지 배워보았다. 다음 포스팅부터는 이를 위한 Distance Measure를 알차게 배워보도록 하자😀😀.  
  
* * *  
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
