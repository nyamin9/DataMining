## 🏆 프로젝트 - Cardio Vascular Data Mining  

💡 사회가 점점 발달함에 따라 우리의 삶이 윤택해지고, 수명이 늘어났습니다. 그럼에도 불구하고 안 좋은 습관
(담배, 술 등)으로 아직 우리는 많은 위험에 노출되어 있는데 그로 인한 큰 위험 중 하나가 심혈관 질환입니다.
이상징후 없이 갑자기 찾아오는 경우가 많은 심혈관 질환은 2019년 통계청의 사망 원인 통계 조사의 결
과 암 다음으로 높은 사망률을 가지는 원인으로 밝혀졌으며, 10만 명당 60.4명의 사망자를 만들 정도로 위험한 질병
입니다. 조용하지만 몹시 치명적이기에 원인을 알고 예방하는 것이 어떤 질병보다 중요합니다. 심혈관 질병을 예방
하기 가장 좋은 방법은 직접 병원에 가 검사를 해보는 것이지만, 바쁜 사람이나 해외에 있는 사람들은 검사를 받
기 힘들 수 있습니다. 따라서 집에서 간단하게 테스트를 해보고 자신이 심혈관 질병이 있는지 알려주는 모델을 만들면 병원에 가야하는 불편함을 줄여줄 수 있을 뿐더러, 혹시나 있을 질병을 예측하는 데 도움이 될 것입니다.<br>  

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

<br>  

## 🏆 프로젝트 결과 해석 및 분석  
  

원본 데이터 test set의 전체 attribute에 대한 Decision Tree의 accuracy가 max_depth=5 일때 0.72439로 가장 높았습니다. Accuracy가 생각보다 낮게 나왔기 때문에 오버피팅을 첫번째 염두에 두고 train set에 대한 accuracy를 산출해 보았습니다. 하지만 max_depth=5 일때 model의 train set에 대한 accuracy 역시 0.726을 조금 상회하는 수준이었고, 이로부터 오버피팅이라기 보다는 학습 자체가 제대로 되지 않았을 가능성이 높다고 생각하였습니다. 다만, 트리의 최대 깊이를 설정하지 않고 default 상태인 None으로 학습을 진행한 경우에는 test set에서 0.642 정도의 accuracy로 그 성능이 더욱 떨어진 것을 확인하였습니다. 이에 그 경우의 train set에 대한 accuracy를 구한 결과 대부분의 수치가 0.9를 상회하는 값이 나왔으며, 확실히 오버피팅이 발생한 것을 확인할 수 있었습니다. 이를 보아 Decision Tree 학습과 테스트에 있어서 Pruning이 중요하다는 것으로 해석할 수 있을 듯 합니다. 반면에, 2절의 연관관계 분석을 통해 추출한 attribute를 통한 accuracy는 전체 attribute에 의한 accuracy와 비슷한 수치를 보여주며 연관관계 분석의 유효함을 입증하였습니다. 또한, 이를 Tree들의 집합인 Random Forest에서 분류하였을 때는 max_depth=12 인 경우에 0.72997 로 소폭 상승했습니다. 여러 개의 트리들을 통해 classification을 한 결과로는 그렇게 좋아보이는 상승량은 아니지만, 성능이 조금이나마 향상되는 것을 확인할 수 있었습니다.  

다음으로는 PCA 분석을 통해 얻은 principal component들을 사용하여 classification을 진행하였습니다. 우선 Decision Tree의 경우에는 max_depth=6에서 가장 높은 accuracy를 가졌으며, 그때의 결과는 0.714 정도였습니다. 따라서 이 경우에도 오버피팅을 생각하고 train set에 대한 accuracy를 산출했으나, 그 경우의 accuracy 역시 0.72를 조금 상회하는 결과가 나왔습니다. 따라서 이 경우에도 학습이 제대로 이루어지지 않았다는 결론을 내릴 수 있었습니다. 또한 max_depth를 None로 설정했을 때에는 train set에 대한 accuracy가 0.99로 완전히 학습에 성공한 반면, test set accuracy는 0.71 정도로 오히려 성능이 살짝 떨어졌습니다. 이 경우 역시 오버피팅이 발생한 것으로 사료되며, pruning의 중요성을 입증한 경우라고 볼 수 있을 것 같습니다. 이어서 진행한 Random Forest에서는 test set에 대한 accuracy가 0.742 정도로 원래 데이터를 사용해서 Random Forest를 수행했을 때보다 높은 성능의 향상을 보여주었습니다. 하지만 이때의 train set에 대한 accuracy가 0.99가 나왔기 때문에 오버피팅이 일어났다고 결론을 내렸습니다. 일반적으로 우리는 test set에 대한 accuracy가 높은 모델을 선호할 수 밖에 없습니다. 아무래도 데이터를 입력했을 때 가장 먼저 눈에 보이는 지표이고, 정답을 많이 예측하는 모델이 우리가 만들기를 원하는 모델이기 때문입니다. 이러한 통념 하에서는 이번 프로젝트에 있어 PCA 분석을 통한 Random Forest 모델이 0.742 정도의 accuracy로 가장 좋은 모델이라고 말할 것입니다. 하지만 이는 모델이 train set에 대해 오버피팅이 일어났다는 사실을 고려하지 않은 결론입니다. 물론 오버피팅이 있더라도 test set의 결과가 눈에 띄게 좋다면 그 모델을 고르는 것이 맞겠지만, 각각의 accuracy들은 분포가 거의 균일한 값들을 가지고 있습니다. 따라서, 바라던 만큼의 좋은 결과가 나오지는 않았으나 위에서 언급한 모델에서 하나를 고른다면 연관관계 분석을 통해 추출한 attribute set (5) 를 사용하여 Random Forest를 수행하였거나, 원본 데이터의 전체 attribute를 가지고 Random Forest를 수행한 모델을 선택하는 것이 최선의 선택이 될 것 같습니다. Accuracy가 그렇게 높게 나오지 않은 이유는 아무래도 object는 많지만 target의 분포가 balanced하고, dimension이 큰 데이터가 아니기 때문일 것입니다. 즉, target의 균일한 분포를 설명하기에는 dimension이 부족했다는 의미입니다. 따라서 굳이 dimensionality reduction을 하지 않아도 모델을 학습시키는 데 무리가 없는, 즉 원본 그 상태로도 정보가 부족했을 가능성이 있는 데이터이지 않을까 생각합니다.  

<br>  

## 🏆 느낀점
수업시간에 배운 다양한 연산들을 실제 코드로 구현하는 것이 재미있었습니다. 또한 데이터의 형태만 맞춰주면 알고 싶은 값을 반환해주는 것을 보고 함수의 내부 구조가 궁금해지기도 했습니다. 특히 단순히 결과를 구하는 것에 그치는 것이 아니라 결과들을 바탕으로 그들간의 관계를 직접 알아내는 경험을 해본 것이 이 프로젝트에서 얻은 가장 큰 수확이라고 생각합니다. 이렇게 체계적으로 데이터를 분석해본 것이 처음이라서 전체적으로 미숙하고, 정해진 루트가 있다기보다는 실제로 사용해야할 방법들을 찾아가면서 임계값을 직접 수정해가며 프로젝트를 수행하는 것이 어려웠습니다. 하지만 대학교에 와서도 이론적인 공부에 지쳐있는 우리에게는 좋은 경험이었다고 생각합니다.  


***
