import sys
input=sys.stdin.readline
N,L=map(int,input().split())
pool=[list(map(int,input().split())) for _ in range(N)]
pool.sort()


for i in range(N):
    pool[i][1]-=1



M=pool[-1][1]
j,count=0,0
pointer=pool[0][0]

while True:

    if pointer<pool[j][0]:
        pointer=pool[j][0]


    while pointer<=pool[j][1]:
       # print(pointer,'널빤지')
        pointer+=L
        count+=1
        
    if pointer>=M:
        break
    j+=1
print(count)