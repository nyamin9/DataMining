# Attribute Noisy 판단
# Systolic / Diastolic Blood Presure Preprocessing 결과 원래 70000개의 row 중 64500개의 row가 남음
# 나머지 column에 대해서 확인작업 진행
# 각 Binary / Ordinal data에 대해 case를 분류하고 데이터수를 비교하여 추가적인 noisy data판단


# 1. Label (cardio) - Binary
# 각 case의 경우의 데이터수의 합이 총 데이터수와 동일 - noisy data 없음
print('cardiovascular : ', len(cardio[cardio['cardio']==1]))
print('Non-cardiovascular : ', len(cardio[cardio['cardio']==0]))
print('Cardio summation : ', len(cardio[cardio['cardio']==1]) + len(cardio[cardio['cardio']==0]))


# 2. Cholesterol - Ordinal
# 각 case의 경우의 데이터수의 합이 총 데이터수와 동일 - noisy data 없음
print('normal-cholesterol : ', len(cardio[cardio['cholesterol']==1]))
print('above normal-cholesterol : ', len(cardio[cardio['cholesterol']==2]))
print('well above normal-cholesterol : ', len(cardio[cardio['cholesterol']==3]))
print('Cholesterol summation : ', len(cardio[cardio['cholesterol']==1]) + len(cardio[cardio['cholesterol']==2]) + len(cardio[cardio['cholesterol']==3]))


# 3. Glucose - Ordinal
# 각 case의 경우의 데이터수의 합이 총 데이터수와 동일 - noisy data 없음
print('normal-Glucose : ', len(cardio[cardio['gluc']==1]))
print('above normal-Glucose : ', len(cardio[cardio['gluc']==2]))
print('well above normal-Glucose : ', len(cardio[cardio['gluc']==3]))
print('Glucose summation : ', len(cardio[cardio['gluc']==1]) + len(cardio[cardio['gluc']==2]) + len(cardio[cardio['gluc']==3]))


# 4. Smoke / Non-smoke - Binary
# 각 case의 경우의 데이터수의 합이 총 데이터수와 동일 - noisy data 없음
print('Smoke : ', len(cardio[cardio['smoke']==1]))
print('Non-smoke : ', len(cardio[cardio['smoke']==0]))
print('Smoke summation : ', len(cardio[cardio['smoke']==1]) + len(cardio[cardio['smoke']==0]))


# 5. Alcohol / Non-Alcohol - Binary
# 각 case의 경우의 데이터수의 합이 총 데이터수와 동일 - noisy data 없음
print('alcohol : ', len(cardio[cardio['alco']==1]))
print('Non-alcohol : ', len(cardio[cardio['alco']==0]))
print('Alcohol summation : ', len(cardio[cardio['alco']==1]) + len(cardio[cardio['alco']==0]))


# 6. Active - Binary
# 각 case의 경우의 데이터수의 합이 총 데이터수와 동일 - noisy data 없음
print('Active : ', len(cardio[cardio['active']==1]))
print('Non-Active : ', len(cardio[cardio['active']==0]))
print('Active summation : ', len(cardio[cardio['active']==1]) + len(cardio[cardio['active']==0]))


# 7. target label 의 분포 확인
# 전체 64,500 개의 사람에 대해서 질환이 없는 경우와 있는 경우를 보았을 떄 32354 : 32146 으로 유사함
# unbalanced한 데이터를 처리하기 위한 방법은 고려하지 않아도 괜찮음
print('질환 없는 사람의 수 : ', len(cardio[cardio['cardio']==0]))
print('질환 있는 사람의 수 : ', len(cardio[cardio['cardio']==1]))


# 8. 데이터 info 확인
cardio.info()


# 9. 최종 데이터 확인
cardio 
