import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
num = list(map(int, input().split()))
q = deque()
l = 0
check = [0]*100001
answer = 0

for i in range(len(num)):
    if not check[num[i]]: # 바로 넣을 수 있음
        check[num[i]] += 1
        answer = max(answer, i-l+1)
    elif check[num[i]]: # 바로 넣지 못하고 k보다 작은지 체크
        if check[num[i]] < k: # 넣을 수 있는 경우
            check[num[i]] += 1
            answer = max(answer, i-l+1)
        else: # 바로 넣을 수 없는 경우
            while check[num[i]] >= k: # 기존 num[i]를 감소시켜야함
                check[num[l]] -= 1
                l += 1
            # 그리고 난 후 삽입
            check[num[i]] += 1
            answer = max(answer, i-l+1)
print(answer)