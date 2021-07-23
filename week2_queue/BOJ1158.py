# 요세푸스 문제

# 1 . 원형 큐 느낌으로 문제 풀이 시작

# 2. 삭제시 삭제한 부분 부터 1번째로 리셋

#3 .출력하는거 list 랑 디큐 차이로 안되는거 같은데 생각해보기
# print("<"+", ".join(str(e) for e in ans)+">")
#리스트로 비교


from collections import deque


N,K = map(int,input().split())

arr = deque([i for i in range(1,N+1,1)])
ans = deque()

for j in range(N):
    for p in range(K-1):
        arr.append(arr.popleft())
    ans.append(arr.popleft())


print("<", end='')
for i in ans:
    if i == ans[-1]:
        print(i, end = '')
    else:
        print("%d, " %(i), end='')
print(">")
