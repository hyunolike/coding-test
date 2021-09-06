# 8주차 Back-tracking

1. 1182 부분수열의 합
2. 9663 N-Queen
3. 13140 Hello World!
4. 7490 0 만들기
5. 1759 암호만들기
6. 6603 로또
7. 1405 미친로봇
8. 2661 좋은 수열
9. [10971 외판원 순회2](#9-10971-외판원-순회)
10. 14888 연산자 끼워넣기
11. 2580 스도쿠
12. 16198 에너지 모으기

## 9. [10971 외판원 순회](https://www.acmicpc.net/problem/10971)
![image](https://user-images.githubusercontent.com/44918665/131620997-df3f81c7-9eed-4e0e-9868-48aa7d16db7f.png)
![image](https://user-images.githubusercontent.com/44918665/131621025-a04ab5fd-18c7-4c6c-a86a-b66e23a9ecd7.png)

### 9.1. 문제 유형
- 백트래킹, 브루트포스

### 9.2. 자료구조
- city (2d-list): 도시 이동 비용을 저장한 2차원 리스트
- visited (list): 도시 방문 여부를 저장한 리스트
- DFS (function):
  - start (int): 출발하는 도시 인덱스
  - total (int): 현재까지 누적한 비용합

### 9.3. 해결과정
1. 0번째 도시부터 1,2,...n-1번째 도시까지 방문 후 다시 0번째 도시로 돌아오는 비용을 기록한다.
2. 해당 비용이 최소비용이라면 출력하고 종료한다.
3. 0번째 도시에서 다른 도시로 출발할 때는, 방문 표시를 한 뒤 출발하며
4. 방문해보고 비용 기록이 끝나면 다시 방문 표시를 제거한 뒤, 다른 도시로도 출발해본다.

### 9.4. 소스코드
```python
n = int(input())
city = [list(map(int, input().split())) for i in range(n)]
visited = [0]*n
answer = 2e10

def DFS(start, total):
    global answer
    if total < answer:
        if all(visited) and start==0:
            answer = min(answer, total)
        for next in range(n):
            if city[start][next]!=0 and not visited[next]:
                visited[next] = 1
                DFS(next, total+city[start][next])
                visited[next] = 0
DFS(0, 0)
print(answer)
```

