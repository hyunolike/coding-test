#2075 N번재 큰수

# 문제풀이 : 1. 단순하게 minheap 사용시 시간초과
# 2.따라서 1.for 문감소 2.for문안에서  조건문사용해서 시간복잡도 감소
#3.1. 2중 for문은 무조건해야되는거 같아서 if 사용해서 최소값만 업데이트 해주자
#4. 어차피 N개의 리스트 갯수안에서 답이 무조건나오기 때문에 이런 알고리즘사용

import heapq
import sys
input = sys.stdin.readline
ans =[]

N = int(input().rstrip())

n=list(map(int,input().split()))
for i in n:
    heapq.heappush(ans,i)

for j in range(N-1):
    n=list(map(int,input().split()))

    for k in n:
        if k > ans[0]:
            heapq.heapreplace(ans,k)

print(heapq.heappop(ans))


