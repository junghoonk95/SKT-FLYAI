머신러닝은 학부시절 지겹게 배운내용이지만 다시 정리 할 수 있는 시간이었던걸로
2년만에 다시보니 반갑기도 하고....

# k-NN 알고리즘

> k-NN 머신러닝을 배우면 가장 처음 나오는 알고리즘이다.  
> 흔히 우리는 “simplest” supervised machine learning algorithms이라 하기도 하는데  
> 그 이유는 단순히 훈련 데이터셋을 그냥 저장하는 것이 모델을 만드는 과정의 전부이기 때문이다  
> 그래서 우리는 k-NN을 "lazy"한 알고리즘으로 분류한다

![image11](https://user-images.githubusercontent.com/80855939/209897933-c38d1a73-b8f1-44e8-86cf-28b9905084e0.png)

위 그림을 보면 ?의 라벨을 찾기위해 근처 라벨된 값을 살피는데, 해당 영역(거리)안에 있는 라벨들의 값들중 다수의 값이 ? 라벨값이 되는 구조이다

![image](https://user-images.githubusercontent.com/80855939/209898838-bba4cb11-4f17-40d9-a248-c5d7b59383d3.png)

위 예시는 k=5로 했을때 보라 삼각형이 3개이기 때문에 ? 값은 보라 삼각형이 되는것을 알 수 있다.

앞서 말했던거처럼 특정 영역 혹은 거리가 기준이라고 했는데

> 거리를 구하는 다양한 방법이 있다. 기본적인 개념이니 설명은 생략

1. 유클리드 거리(Euclidean distance)  
가장 흔하게 사용하고 기본적이 거리법이다  
![image](https://user-images.githubusercontent.com/80855939/209903929-f3ae86b3-1bdb-4e3e-9003-ef80cc5db338.png)

2. 맨해튼 거리법   
절대값을 이용한 거리법  
![image](https://user-images.githubusercontent.com/80855939/209903886-22e11aa8-9696-46b8-a8f8-932b6b868bdc.png)

3. 민코스키 거리(Minkowski distance)  
유클리드 거리법과 반대로 민코스키 거리는 가장 큰 차이만을 이용하기 때문에 0에 가까울수록 유사  
![image](https://user-images.githubusercontent.com/80855939/209903911-e9d7dcc0-7d49-46bb-adb2-bca5ae6db506.png)


*추가적으로 우리는 동률을 피하기위해 k값은 보통 홀수 지정해준다*


> k-NN 알고리즘을 배울대 교수님이 "Curse of Dimensionality"(차원의 저주)라는 개념을 설명해 주셨던것으로 기억나는데 몹시 강조하셔서 설명 해보면  
> 차원이 많은 데이터(변수)에서는 학습데이터 수가 차원 수보다 적어져서 성능이 저하되는 현상이 나타 날 수 있다는 점이다.  
> 차원이 늘어나면 점과 점사이의 공백이 넓어지기 때문에 bias를 야기 할 수 있기 때문이다.  
> 그래서 이러한 경우에는 다른 알고리즘을 쓰는것을 추천드리거나 변수를 줄이는 기법(PCA나 중요한 변수만 뽑아낸다는지 등)을 활용 하면 되겠다


# SVM 알고리즘
