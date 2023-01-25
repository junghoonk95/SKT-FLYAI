import pprint
N,M,K=map(int,input().split())
arr=[[[(0,0,0)] for i in range(N)] for i in range(N)]
new_arr=[[[(0,0,0)] for i in range(N)] for i in range(N)]
for i in range(M):
    r,c,m,s,d=map(int,input().split())
    arr[r-1][c-1]=[(m,s,d)]
    # past_arr[r-1][c-1]=[(m,s,d)]

# pprint.pprint(arr)

def move():
    new_arr = [[[(0, 0, 0)] for i in range(N)] for i in range(N)]
    nx=[0,1,1,1,0,-1,-1,-1]
    ny=[1,1,0,-1,-1,-1,0,1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != [(0, 0, 0)]:
                m,s,d=arr[i][j][0]
                print((i+ny[d]*s)%N,(j+nx[d]*s)%N,i,j)
                new_arr[(i+ny[d]*s)%N][(j+nx[d]*s)%N].append((m,s,d))
    return new_arr

pprint.pprint(move())
# pprint.pprint(move()[0][2])
pprint.pprint(new_arr)
# def meet(i,j,new_arr):
#     new_arr[i][j]
#
#     return new_arr
# pprint.pprint(meet(0,2,new_arr))
