import sys
input=sys.stdin.readline


N,K,Q,M=map(int,input().split())
Klist=list(   map(int,input().split())    )
Qlist=list(   map(int,input().split())    )
section=list(   list(map(int,input().split())) for _ in range(M)    )

student=[1 for _ in range(1,N+3)]

for i in range(Q):
    j=Qlist[i]
    if j in Klist:
        continue
    while j-1<len(student):
        if j in Klist:
            j+=Qlist[i]
        else:
            student[j-1]=0
            j+=Qlist[i]


sum=0
prefix=[0]
for i in range(len(student)):
    sum+=student[i]
    prefix.append(sum)

for a,b in section:
    print(prefix[b]-prefix[a-1])
