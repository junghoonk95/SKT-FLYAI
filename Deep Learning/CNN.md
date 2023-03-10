# 합성곱 신경망(CNN)

  - 음성인식이나 이미지 인식에서 주로 사용되는 신경망의 한종류

  - 수학적 연상을 사용해서 이미지의 특성을 추출하는 레이어를 포함

  - 이미지 처리에 탁월한 성능을 보이는 신경망
    - 다차원 배열 데이터를 처리하도록 구성
    - 컬러 이미지와 같은 다차원 배열 처리에 특화됨
      - 이미지 인식 분야에서 딥러닝을 활용한 기법은 대부분 CNN을 기초로함

## 신경망(NN)
  - 이미지 전체를 하나의 데이터로 생각 -> 입력으로 받아드립
  - 이미지의 특성을 찾지 못하고 이미지의 위치가 조금만 달라지거나 왜곡된 경우 올바른 성능을 내지 못함

## 합성곱 신경망 (CNN)
  - 이미지를 하나의 데이터가 아닌 여러 개로 분할하여 처리함
  - 이미지가 왜곡되더라도 이미지의 부분적 특성을 추출 할 수 있음

## 합성곱 신경망 구조
  - 여러계층을 조합, 다만 일반적인 신경망과는 다르게, 합성공 계층(Convolutional Layer)와 풀링 계층 (Pooling Layer)이 추가 (Pooling Layer은 생략가능)
  - 출력과 가까운 층에서는 "RELU" 계층 구성을 사용, 마지막 계층은 Softmax

![image](https://user-images.githubusercontent.com/80855939/210292063-905e7db1-8c48-4997-b160-f9b250b4df73.png)


## 합성곱 계층
  - 이미지와 같은 3차원 데이터를 입력 받으면 다음 계층에도 3차원 데이터로 전달
  - 특징맵(Feature Map): 합성곱(Convolution Layer) 계층의 입출력 데이터
    - 입력 특징맵(input feature map) : 입력데이터
    - 출력 특징맵 (Output Feature Map) : 출력 데이
  
  - 합성곱 연상
    - 필터 사이즈: 가로, 세로 크기를 갖게함 출력크기 조절
    - 스트라이트: 필터가 이미지에 적용될때 한번에 움직이는 픽셀 설정 (이동하는 간격)
    - 패딩: 합성곱 연상을 수행하기 전에 입력 데이터 주변은 특정값(0,1등)으로 채우기
![image](https://user-images.githubusercontent.com/80855939/210292796-bd6e1327-151d-484b-ab3e-02ec6a0af5ff.png)



  ![image](https://user-images.githubusercontent.com/80855939/210292599-d319aae2-5cd5-4a1a-9a69-329e72bccb68.png)


## 폴링계층

  - 2차원 데이터의 세로 및 가로 방향의 공간을 줄이는 연산
  - 최대 풀링(Max Pooling),평균 풀링(Average Pooling)
    - 최대 풀링 : 대상 영역에서 최대값을 취하는 연산
    - 평균 풀링 : 대상 영역에서 평균값을 취하는 연산
    
## 풀링 계층 특징
  - 풀링 계층은 합성곱 계층과 달리 학습해야 할 매개변수가 없음
  - 풀링은 대상 영역에서 최대값이나 평균을 취하는 명확한 처리임으로 특별히 학습할 것이 없음
  - 풀링 연산은 입력데이터의 채널 수 그대로 출력 데이터로 전달
  - 풀링은 2차원 데이터의 크기를 줄이는 연산이므로 3차원을 결정하는 채널 수는 건드리지 않음(채널마다 독립적 계산)
  - 입력의 변화에 영향을 적게 받음
  - 입력 데이터가 조금 변하더라도 풀링 계층 자체가 그 변화를 흡수하여사라지게함


## 일반화(Generalization)
  - 많은 경우에 Generalization(일반화) 성능을 높이는 것이 목적
  - 일반화의 동작 여부
    - Train 거듭할 수록 train error 는 감소, Test error는 그렇지 않음
    - Training error 와 Test error의 차이를 Generalization performance
    - Generalization 이 좋다는 의미는 네트워크의 성능이 학습 데이터와 비슷하다를 보장한다는것
      - Train error 와 test error 의 gap이 적다
  - But, 애초에 학습데이터의 퍼포먼스가 좋지 않다면,
    - 아무리 Generalization이 좋다 하더라도 네트워크의 성능이 좋지 않음



## 드롭아웃(Dropout)
- 일부를 무작위하게 제거하면 뉴런의 부정한 협업을 제거, 무작위하게 제거하면 노이즈가 추가됨
- 만약 Dropout 없으면 뉴런끼리의 우연한 패턴을 기억-> 주로 0.2~0.5

## CNN overfitting 방지
- 훈련데이터 증가
- 네트워크의 용량을 감소
- 가중치 규제를 추가
- 드롭아웃 추가 


배치 정규화
