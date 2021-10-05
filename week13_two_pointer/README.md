# Two Pointer

1. [22114 창영이와 점프](#1-22114-창영이와-점프)
2. 7453 합이 0인 네 정수
3. 16161 가장 긴 증가하는 팰린드롬 부분수열
4. 20922 겹치는 건 싫어
5. 2003 수들의 합 2
6. 1806 부분합
7. 22862 가장 긴 짝수 연속한 부분 수열(large)
8. 22945 팀 빌딩
9. 2531 회전 초밥
10. 2230 수 고르기

## 1. [22114 창영이와 점프](https://www.acmicpc.net/problem/22114)
![image](https://user-images.githubusercontent.com/44918665/135942246-1b2554eb-c7ff-4dbb-bc63-bd5598c76491.png)
![image](https://user-images.githubusercontent.com/44918665/135942302-28c36f8a-599a-49a1-bb42-f0a4ce2fa60f.png)
![image](https://user-images.githubusercontent.com/44918665/135942321-0098edd3-0f9f-4753-9280-944c53e2f458.png)

### 1.1. 문제유형
- 두 포인터

### 1.2. 해결과정
1. 거리가 k 이하면 r, cnt를 증가시킨다.
2. 거리가 k 이상이면 jump하고 r, cnt를 증가시킨다.
3. jump를 이미 했다면 l++, cnt--를 반복하며 점프한 구간을 배제한다.
4. jump한 구간을 삭제하고 새롭게 r, cnt를 증가시킨다.
5. loop마다 answer에 cnt 최대값을 누적한다.

### 1.3. 소스코드
```python
import sys
input = sys.stdin.readline

n,k=map(int, input().split())
brick=list(map(int, input().split()))
l, r = 0, 0
answer, cnt = 1,1
jump=1
while True:
    if l >= n-1 or r >= n-1:
        break
    if brick[r]<=k:
        cnt += 1
        r += 1
    elif brick[r]>k:
        if jump:
            jump -= 1
            cnt += 1
            r += 1
        else:
            while brick[l]<=k:
                l += 1
                cnt -= 1
            if brick[l]>k:
                l += 1
                cnt -= 1
            r += 1
            cnt += 1
    answer = max(answer, cnt)
print(answer)
```

## 2. 7453 합이 0인 네 정수
## 3. 16161 가장 긴 증가하는 팰린드롬 부분수열
## 4. 20922 겹치는 건 싫어
## 5. 2003 수들의 합 2
## 6. 1806 부분합
## 7. 22862 가장 긴 짝수 연속한 부분 수열(large)
## 8. 22945 팀 빌딩
## 9. 2531 회전 초밥
## 10. 2230 수 고르기
