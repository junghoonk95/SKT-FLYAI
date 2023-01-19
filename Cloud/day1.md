# Abstract Version

Azure 가입

Hyper -V 체크

가상컴퓨터 만들

리소스 만들기 -> 가상머신 -> 

Could Computing


DevOps combines development and operations to increase the efficiency, speed, and security of software development and delivery compared to traditional processes. 
A more nimble software development lifecycle results in a competitive advantage for businesses and their customers.


MS Azure

1.ubuntu 20.04

2.window server 2022 datacenter 이미지

Cloud = Virtualization(server+storage+Network) + Network
-> rdp (cmd 아님)

가상머신->네트워크->인바운드 포트 규칙->http 추
IIS

3.


VM Scale Set(가상 머신 확장 집합) 만들기

수직크기 조정 Scaling up 2

수평크기 조정 Scaling out 1+1


1.부하 분산 장치
-> 하나의 ip 여러서


서버 ------>ip주소---------------> ->가상머신1
              (공용 부하분산 장치) ->가상머신2
              
              
2. VMSS


초기 인스턴스 수

https://tecoble.techcourse.co.kr/post/2021-10-12-scale-up-scale-out/
              
특정 규칙(트리거)에 의거 scaling out/in 
https://learn.microsoft.com/ko-kr/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-autoscale-portal




      ISP (sk 브로드밴드)
  
      Wan

Lan1        Lan2

IPv4

255.255.255.255
8bit X4

subnet mask
Myvnet 생성 -> 이때 subnet mask 추가
>create Vm 머신 2개 그리고 동일 Myvnet 이
