---
title : "🧩 Data Mining (6) - Distance_3 : Minkowski"

categories:
    - Data_mining
tags:
    - [Pandas, Data, Data Mining, Distance, Numerical, Minkowski]

toc : true
toc_sticky : true
use_math : true

date: 2022-07-03
last_modified_at: 2022-07-03
---  
* * *  

🧩 저번 포스팅에서는 categorical data에 대한 distance measure를 알아보았다. 이번에는 <a>Numerical Data</a>를 위한 measure인 <b><a>Minkowski Distance</a></b>를 배워보도록 하자.  
  
## 1. Basic Minkowski Distance  
  
👉 Minkowski Distance 역시 두 object들 사이의 distance를 계산할 때 사용된다. 예를 들면,<br>  

<p align="center"><img src="https://user-images.githubusercontent.com/65170165/177021852-d41ca238-7aca-4939-9f34-063ea6b03901.png" width="600" /></p>  
  
이와 같이 $l$개의 feature를 가진 데이터의 모든 feature에 대해서 Basic Minkowski Distance는 아래와 같이 정의된다.<br>  
  
<center>$d(i,j)\;=^p\sqrt{|x_{i1}-x_{j1}|^p+|x_{i2}-x_{j2}|^p+...+|x_{il}-x_{jl}|^p}$</center><br>  

그리고 이떄의 $p$값에 대해서 Minkowski Distance를 <b><a>$L-p\;norm$</a></b> 이라 한다.  
  
Minkowski Distance 는 몇가지 성질을 가지고 있는데,  
- $d(i,j)>0\;\;(when\;\;i\neq{j})$<br>  
- $d(i,i)=0\;\;\,(positivity)$<br>  
- $d(i,j)=d(j,i)\;\;(symmetry)$<br>  
- $d(i,j)\leqq{d(i,k)}+d(k,j)\;\;(Triangle\;Inequality)$<br>  
  
맨 마지막 성질이 이해가 안 갈 수 있는데, 이는 $i,j,k$ 세 점이 삼각형을 이룰 때라고 생각하면 된다. 한 변의 길이가 두변의 길이의 합보다 작아야 한다는 삼각형의 생성조건에 의한 성질이다.  

🧩 위에서 언급했듯이 Minkowski distance는 $p$값에 의해 수식과 이름이 달라진다. 이제는 그 경우에 대해 알아보도록 하자.  

* * *  
## 2. L-p Norm  

- p = 1 인 경우  
    - L<sub>1</sub> Norm, <b><a>Manhattan Distance</a></b>  
    - 단순 거리의 크기의 합.  

<center>$d(i,j)\;=|x_{i1}-x_{j1}|+|x_{i2}-x_{j2}|+...+|x_{il}-x_{jl}|$</center>  

- p = 2 인 경우  
    - L<sub>2</sub> Norm, <b><a>Euclidean Distance</a></b><br>  
    - 흔히 수학에서 접할 수 있는 두 점 사이의 거리 공식.  
  
<center>$d(i,j)\;=\sqrt{|x_{i1}-x_{j1}|^2+|x_{i2}-x_{j2}|^2+...+|x_{il}-x_{jl}|^2}$</center><br>  

- p  $\rightarrow$ ∞ 인 경우  
    - L<sub>max</sub> Norm, L<sub>∞</sub> Norm, <b><a>Supremum Distance</a></b>  
    - 거리의 크기들 중 최댓값을 선택.  

<center>$d(i,j)\;=max(|x_{i1}-x_{j1}|,\,|x_{i2}-x_{j2}|,\,...,\,|x_{il}-x_{jl}|)$</center><br>  

🧩 당연히, 이 Mimkowski Distance의 결과 역시 Distance Matrix의 형태로 만들어 줄 수 있다. 관련 링크를 첨부해 두었으니 필요한 사람은 참고해도 좋을 것 같다😊.  

[📝 Distance Matrix 관련 포스팅](https://nyamin9.github.io/data_mining/Data-Mining-Distance-1/).  

* * *  

🧩 이번 포스팅에서는 Numerical Attribute의 distance measure를 다뤄보았다. 수식에 루트도 들어가 있어서 약간 귀찮아보일 수 있지만, 그 방식은 생각보다 간단하기 때문에 직접 구현해 보는 것도 어렵지 않을 것이라 생각한다. 다음 포스팅에서는 Document frequency를 위한 distance measure를 배워보자🏃‍♂️🏃‍♂️.  

* * *  
<div style="text-align: left">💡위 포스팅은 한국외국어대학교 바이오메디컬공학부 고윤희 교수님의 [생명정보학을 위한 데이터마이닝] 강의 내용을 바탕으로 함을 밝힙니다.</div>
