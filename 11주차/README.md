
# [week11] [구간 합 구하기5] 발표자료

## 1. [11660] [구간 합 구하기5]
![스크린샷 2021-09-22 오후 11 36 06](https://user-images.githubusercontent.com/64303390/134364263-66033f44-2a29-4e23-a1e3-9b38702267a2.png)


### 1.1 문제유형
- 누적합

### 1.2 풀이과정
1. 입력받은 표에 대해 행 별로 누적합을 구한다.
2. 입력받은 좌표를 x1과 x2 좌표 만큼 순회하며 결과를 합산한다
3. 결과를 출력한다.

### 1.3 소스코드

```python
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
square=[list(map(int,input().split())) for _ in range(N)]
op=[list(map(int,input().split())) for _ in range(M)]


squareSum=[[0]*(N+1) for _ in range(N)]


for i in range(N):
    temp=0
    for j in range(N):
        temp+=square[i][j]
        squareSum[i][j+1]=temp


for x1,y1,x2,y2 in op:
    res=0
    for i in range(x1,x2+1):
        res += (squareSum[i-1][y2] - squareSum[i-1][y1-1])
    print(res)

```

