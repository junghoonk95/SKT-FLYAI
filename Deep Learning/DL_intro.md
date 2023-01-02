# 심층 신경망
- 입력층(input layer)과 출력(output layer)층 사이에 여러개의 은닉(hidden layer)층 들로 이뤄진 인공신경망(ANN)
- 복잡한 비선형 관계(non-linear relationshipo)들을 모델링
- 심층 학습 구조들을 순환 신경명(RNN)에 적용
- 컴퓨터비젼, 자동음성인식,을 위한 모델링 분야에 적용


Input layer(입력층): 네트워크의 입력 부분 학습 시키고 싶은 X값

Hidden layers(은닉층): 입력층과 층력층을 제외한 중간층, 은닉층은 완전연결



## 오차 역전파

순전파와는 반대로 출력층에서 입력층 방향으로 계산하면서 가중치를 업데이트

## 경사 하강법

함수의 기술기(경사)를 구하여 기울기가 낮은 쪽으로 계속 이동시켜서 극값에 이를 때까지 반복시키는것

## 손실함수

가중치에 따라 오차가 얼마나 커지거나 작아지는가를 평가

### - 평균 제곱오차(MSE)
실제값과 추정값과의 차이를 나타내며 회구문제에 사용됨

### - 교차 엔트로피 함수(Cross - Entropy Error CEE)
두분포간의 차이를 나타내는 척도로서 분류문제에 많이 사용됨

### - 경사도 손실문제
- 경사도 소실
1. 여러 은닉 계층으로 구성되어 활성화 함수에 따라 경사도 소실이 발생할 수 있음
2. 실제값과 추정갑과의 차이를 나타내며 회귀문제에 사용됨
3. DNN 에서는 경사도 소실 문제를 극복하는 함수로 ReLU 활성화 함수 사용


![image](https://user-images.githubusercontent.com/80855939/210188429-3bf81bf2-f5ac-4513-a5c8-c4d9cbf91e20.png)


## DNN 구현 단계

> DNN 구현단계 -> Dense Module -> Dropout

- DNN 구현단계
1. 기본 파라미터 설정
2. 분류,회귀 DNN 모델 구현
3. 데이터 준비
4. DNN 학습 및 성능평가


- Dense Module
1. Neural Network를 구성하는 Layer를 todtjdgkf Eo tkdyd
2. model.add(Dense(1,input_dim=3,activation ="relu")
3. -첫번째 인자: 출력 노드의수
4. input_dim:입력 노드의 수(입력의 차원)
5. activation 활성화 함수
 
**가지고 있는 데이터에 따라 활성화 함수 설정 !** 

- Dropout
1. 일부의 노드를 생략한 후에 학습을 진행

# 단순 선형회귀

## 완전 연결층을 사용해 단순 선형회귀


