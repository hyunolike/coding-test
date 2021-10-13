# Dynamic Programming

1. [2938 설탕배달](#1-2938-설탕배달)
2. [1463 1로 만들기](#2-1463-1로-만들기)

## 1. [2938 설탕배달](https://www.acmicpc.net/problem/2938)
![image](https://user-images.githubusercontent.com/44918665/137054011-dd2ce662-bf28-4499-989e-bb1ea4839c3a.png)
![image](https://user-images.githubusercontent.com/44918665/137054038-d9bc0d78-51f4-4e48-9999-e7b3f46ebbb6.png)

### 1.1. 문제유형
- dp

### 1.2. 해결과정
1. 개수를 줄이기 위해선 5로 최대한 나누어야 한다.
2. 5로 나눌 수 없을 때 3을 한 번씩 뺀다.
3. 1-2를 반복하며 answer를 카운트한다.
4. 만약 결과가 0이 아니라면 -1을 리턴한다.

### 1.3. 소스코드
```python
n=int(input())

answer=0
while n>=0:
    if n%5==0:
        answer+=n//5
        n=0
        break
    else:
        n-=3
        answer+=1
if n!=0:
    answer=-1
print(answer)
```

## 2. [1463 1로 만들기](https://www.acmicpc.net/problem/1463)
![image](https://user-images.githubusercontent.com/44918665/137054264-eda046ca-3ca8-4e4f-aadf-8d160a957fb8.png)
![image](https://user-images.githubusercontent.com/44918665/137054303-ee579b3f-0506-4976-b2a1-561ee29192e8.png)

### 2.1. 문제유형
- dp

### 2.2. 해결과정
1. i=2~n까지 될 수 있는 최소 연산 수를 누적한다.
2. dp[i]=dp[i-1]+1이다. (2에서 3이 되려면 1증가시키면 되기 때문)
3. 단, i가 2의 배수일 경우 dp[i//2]에서 dp[i]로 올 수 있다.
4. 또한, i가 3의 배수일 경우 dp[i//3]에서 dp[i]로 올 수 있다.
5. 따라서 dp[i-1]+1, dp[i//2]+1(i가 2의배수), dp[i//3]+1(i가 3의배수) 최솟값을 누적한다.
6. dp[n]을 출력한다.

### 2.3. 소스코드
```python
n=int(input())
dp=[0]*(n+1)

for i in range(2, n+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)
print(dp[n])
```





