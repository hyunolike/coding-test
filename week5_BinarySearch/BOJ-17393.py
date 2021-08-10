# 17393 다이나믹 롤러

#칠할수있는 최대 칸수를 구해보자


# 문제 풀이:

import sys
input = sys.stdin.readline

N = int(input().rstrip())

Ink = list(map(int,input().rstrip().split()))

Viso = list(map(int,input().rstrip().split()))
k= 0
ans = []

for i in range(N):
    start = i+1
    end = N-1
    temp = Ink[i]


    while start <= end:
        mid = (start+end) // 2
        if temp <Viso[mid]:
            end = mid-1
            k = end
        else:
            start = mid+1
            k = mid
    
    ans.append(k-i)

print(ans)
