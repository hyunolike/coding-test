#1158 좋은친구
#1. 첫번째 풀이 for 2개 중첩으로 풀이 -> 시관초과

#2 디큐활용 하여 슬라이딩 윈도우 구현

#3  길이를 중점으로 구현하여 N 사용 1회 감소 

#4  혼자 힘으로 해결 못했던 문제이므로 추후 한번 다시보기 (볼시 삭제)

from collections import deque

N,K = map(int,input().split())
arr = []
answer = 0
for i in range(N):
    arr.append(len(input().strip()))
    
num = [0 for i in range(22)]


for i in range(3, 22):
    arr2 = deque()
    for word in arr:
        arr2.append(word)
        if len(arr2) > K + 1:
            if arr2.popleft() == i: 
                num[i] -= 1
        if word == i:
            if num[i] > 0:
                 answer += num[i]
            num[i] += 1
    
print(answer)    
