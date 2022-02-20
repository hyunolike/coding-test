import sys
import copy
input=sys.stdin.readline
M,N=map(int,input().split())
K=int(input())
Map=[list(input().split()) for _ in range(M)]
area=[list(map(int,input().split())) for _ in range(K)]



sumlist=[[[0,0,0] for _ in range(N+1)] for _ in range(M)]


for i in range(M):
    for j in range(N):
        sumlist[i][j+1]=copy.deepcopy(sumlist[i][j])
        if Map[i][0][j]=='J':
            sumlist[i][j+1][0]+=1
        elif Map[i][0][j]=='I':
            sumlist[i][j+1][2]+=1
        elif Map[i][0][j]=='O':
            sumlist[i][j+1][1]+=1

for a,b,c,d in area:
    ans=[0,0,0]
    for abc in range(a-1,c):
        for i in range(3):
            ans[i]+=sumlist[abc][d][i]-sumlist[abc][b-1][i]
    print(ans[0],ans[1],ans[2])