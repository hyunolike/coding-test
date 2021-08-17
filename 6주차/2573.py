import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
N,M=map(int,input().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

ice=[ list(map(int,input().split()))  for _ in range(N) ]

graph=[ [0]*M for _ in range(N) ]

def numberOfIce(x,y):
    stack[x][y]=-1
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if (0<=mx<N) and (0<=my<M) and stack[mx][my]!=-1 and ice[mx][my]>0:
            numberOfIce(mx,my)
count=0
stack=[ [0]*M for _ in range(N) ]
for a in range(1,N-1):
    for b in range(M):
        if stack[a][b]!=-1 and ice[a][b]>0:
            numberOfIce(a,b)
            count=count+1
if count>=2:
    print(0)
    sys.exit()






for abcd in range(45):
    for a in range(N):
        for b in range(M):
            for j in range(4):
                mx=a+dx[j]
                my=b+dy[j]
                if (0<=mx<N) and (0<=my<M) and (ice[a][b]>0):
                    if ice[mx][my]<=0:
                        graph[a][b]-=1
    temp=[ [0]*M for _ in range(N) ]
    for i in range(1,len(ice)-1):
        for j in range(len(ice[0])):
            temp[i][j]=ice[i][j]+graph[i][j]
    ice=temp

    stack=[ [0]*M for _ in range(N) ]
    count=0
    for a in range(1,N-1):
        for b in range(M):
            if stack[a][b]!=-1 and ice[a][b]>0:
                numberOfIce(a,b)
                count=count+1
    flag=True
    if count>=2:
        print(abcd+1)
        break
    else:
        for a in range(1,N-1):
            for b in range(1,M-1):
                if ice[a][b]>0:
                    flag=False
                    break
        if flag:
            print(0)
            break
    
    graph=[ [0]*M for _ in range(N) ]
