https://learn.microsoft.com/ko-kr/azure/container-instances/container-instances-tutorial-prepare-app

https://learn.microsoft.com/ko-kr/cli/azure/install-azure-cli

# Windows에 Azure CLI 설치후 AZ 로그인

[윈도우 Azure CLI](https://aka.ms/installazurecliwindows)
>설치확인
```
>AZ 로그인
```

az login
```



![image](https://user-images.githubusercontent.com/80855939/217418461-663a7540-f7ee-4336-8d61-6ebeaabfa6ae.png)


> Azure 로그인


> 간단한 웹앱 다운
git clone https://github.com/Azure-Samples/aci-helloworld.git

> 컨테이너 이미지를 만들고 aci-tutorial-app으로 태깅
* 다운 받은 폴더에서 진행, 도커가 실행 되어있는 상태여야함

```
docker build ./aci-helloworld -t aci-tutorial-app
```
![image](https://user-images.githubusercontent.com/80855939/217412905-ccd63fc3-2a2d-4c39-b1c8-22d33628dfed.png)

> docker images
![image](https://user-images.githubusercontent.com/80855939/217417945-ac7baeb0-8744-4466-9646-3d1d30911b2e.png)
![image](https://user-images.githubusercontent.com/80855939/217417995-b385d3d6-9e1b-482c-8368-cfbad571a4a8.png)



## 컨테이너 실행
```
docker run -d -p 8080:80 aci-tutorial-app
```

![image](https://user-images.githubusercontent.com/80855939/217413691-e86e29ba-84e8-4e10-be00-68d08b641ba4.png)
