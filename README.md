# 🐍 Data-Mining  

🐣 2022-1 학기 데이터마이닝 정리 / 프로젝트 내용 정리  

🎬 2022. 09. 01 ~  

***  

## 2022년 1학기에 배운 데이터마이닝 강의의 수업 이론과 프로젝트 진행과정을 기록할 레퍼지토리입니다.  

- 이론이 굉장이 방대하고 손필기로 공부한 까닭에 기록 주기가 그렇게 짧지는 않을 것 같습니다. 그래도 열심히 기록해 보겠습니다.<br>  
  
  
- 프로젝트의 경우 각 해당하는 파트에 맞게 제목을 지어둘 예정이며, plotly를 통해 시각화하여 반응형 그래프를 관찰 할 수 있습니다.
  - 다만 깃허브 레퍼지토리는 인터랙티브한 plot을 지원해주지 않기 때문에, 해당 그래프의 임베딩 URL을 클릭하여 확인하시면 좋을 것 같습니다.
  - 운영중인 깃허브 블로그에도 올라갈 예정입니다. 블로그에서는 URL을 누르지 않으셔도 확인하실 수 있으니, 이 방법이 훨씬 편할 수 있을 듯 합니다😊.
  - 블로그 주소는 https://nyamin9.github.io/ 입니다!! 제 깃허브 readme에도 링크가 걸려있습니다.  
    
<br>  
<br>  

## 🏆 프로젝트 - Cardio Vascular Data Mining  

💡 사회가 점점 발달함에 따라 우리의 삶이 윤택해지고, 수명이 늘어났습니다. 그럼에도 불구하고 안 좋은 습관
(담배, 술 등)으로 아직 우리는 많은 위험에 노출되어 있는데 그로 인한 큰 위험 중 하나가 심혈관 질환입니다.
이상징후 없이 갑자기 찾아오는 경우가 많은 심혈관 질환은 2019년 통계청의 사망 원인 통계 조사의 결
과 암 다음으로 높은 사망률을 가지는 원인으로 밝혀졌으며, 10만 명당 60.4명의 사망자를 만들 정도로 위험한 질병
입니다. 조용하지만 몹시 치명적이기에 원인을 알고 예방하는 것이 어떤 질병보다 중요합니다. 심혈관 질병을 예방
하기 가장 좋은 방법은 직접 병원에 가 검사를 해보는 것이지만, 바쁜 사람이나 해외에 있는 사람들은 검사를 받
기 힘들 수 있습니다. 따라서 집에서 간단하게 테스트를 해보고 자신이 심혈관 질병이 있는지 알려주는 모델을 만들
면 병원에 가야하는 불편함을 줄여줄 수 있을 뿐더러, 혹시나 있을 질병을 예측하는 데 도움이 될 것입니다.<br>  

<p align="center"><img src="https://user-images.githubusercontent.com/65170165/200470962-f08bc143-a80a-48f8-ab25-7766920fc2d1.jpg" width="500" /></p>  

<p align="center"><사망원인 통계 조사, 통계청, 2019></p>    
  
💡 저희가 원하는 심혈관 질환 발병 모델은 사용자가 자신의 정보를 입력하면 다른 환자의 정보들로부터 학습된
심혈관 질환 모델이 사용자의 심혈관 질병의 발병 여부에 대해 예측하고 결과를 알려주는 것입니다. 이러한 심혈관 질환 발병 확인 모델을 만들기 위해 첫번째로 noisy data나, missing data를 찾아서 수정을 하는 데이터 전처리를 할 것입니다. 두번째로 attribute들의 상관관계를 조사해서 비교적 상관관계가 적은 attribute들을 제거해 보고, 선택된 attribute를 가지고 attribute set을 만들 것입니다. 마지막으로 수정된 data를 가지고 decision 
tree 와 random forest classification으로 model의 성능을 알아볼 예정입니다.  
  
<br>  
<br>  
  
  
## 프로젝트 plotly 차트보드 주소  
  
[📊 01. 데이터 전처리 01](https://chart-studio.plotly.com/~nyamin9/64)  

[📊 02. 데이터 전처리 02-노이즈 판단 및 분포 파악](https://chart-studio.plotly.com/~nyamin9/70)

[📊 03. 데이터 attribute 간 상관관계 분석](https://chart-studio.plotly.com/~nyamin9/66)

[📊 04. PCA 분석](https://chart-studio.plotly.com/~nyamin9/63)  

[📊 05. Classification (결정트리/랜덤포레스트)](https://chart-studio.plotly.com/~nyamin9/71)  

[📊 06. 결과레포트](https://github.com/nyamin9/Data-Mining/blob/main/Project/14.%202022-1%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A7%88%EC%9D%B4%EB%8B%9D%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EA%B2%B0%EA%B3%BC%20%EB%A0%88%ED%8F%AC%ED%8A%B8.pdf)
  
<br>  
  
***

(2022.11.07 추가)  
  

📌 기존에 제가 블로그나 깃허브에 plotly그래프를 호출하는 방식은 plotly 계정의 API key 값을 사용해서 그래프에 대한 링크를 임베딩하는 방식입니다. 그런데 저의 plotly Home 대쉬보드에 더 이상의 여유공간이 없어서,,,!! (몇 개 올린 것 같지도 않은데 말이죠...😥😥) 더 이상 그래프를 호출을 못하더라구요,,, 그래서 다른 방법을 찾는 중이었습니다.<br>  

📌 어떡해야 할까 정말 많은 고민을 했는데 찾은 방법은 plotly에 업로드 하는 것이었습니다. 제가 주피터로 작성한 파이썬 코드를 업로드하면 그 plotly 그래프 결과도 볼 수 있어 나쁘지 않은 방법이라고 생각합니다.<br>  

📌 시각화를 진행한 .ipynb 파일은 업로드해서 readme에 남겨두겠습니다. 아래의 링크를 타고 들어오시기를 바랍니다!!<br>  
  
<br>  
  

[📊 01. 데이터 전처리 01](https://chart-studio.plotly.com/~nyamin9/64)  

[📊 02. 데이터 전처리 02-노이즈 판단 및 분포 파악](https://chart-studio.plotly.com/~nyamin9/70)

[📊 03. 데이터 attribute 간 상관관계 분석](https://chart-studio.plotly.com/~nyamin9/66)

[📊 04. PCA 분석](https://chart-studio.plotly.com/~nyamin9/63)  

[📊 05. Classification (결정트리/랜덤포레스트)](https://chart-studio.plotly.com/~nyamin9/71)  

[📊 06. 결과레포트](https://github.com/nyamin9/Data-Mining/blob/main/Project/14.%202022-1%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A7%88%EC%9D%B4%EB%8B%9D%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EA%B2%B0%EA%B3%BC%20%EB%A0%88%ED%8F%AC%ED%8A%B8.pdf)


***  

🚩 빠르다고는 장담할 수 없을 것 같지만, 꾸준히 성장하는 DA가 되기 위해 노력하겠습니다.   
