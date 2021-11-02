import heapq

n,m,k=map(int,input().split())
value=list(map(int, input().split()))
heap=[]
for v in value:
    heapq.heappush(heap, -v)
first=heapq.heappop(heap)*(-1)
second=heapq.heappop(heap)*(-1)

answer,cnt=0,0
while m>0:
    if cnt==k:
        answer+=second
        cnt=0
        m-=1
        continue
    answer+=first
    cnt+=1
    m-=1
print(answer)

# another solution
n,m,k=map(int, input().split())
data=list(map(int, input().split()))

data.sort()
first=data[-1]
second=data[-2]

count=int(m/(k+1))*k
count+=m%(k+1)
result=0
result+=(count)*first
result+=(m-count)*second
print(result)
