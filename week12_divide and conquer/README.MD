# [12주] [Divide and Conquer] 발표자료
1. [2339 석판 자르기](#1-2339-석판-자르기)

## 1. [2339 석판 자르기](https://www.acmicpc.net/problem/2339)
![2021-09-29 (1)](https://user-images.githubusercontent.com/69501435/135285599-122f9b21-aea2-4c11-9502-22bdfdce2e9a.png)

### 1.1 자료구조
1. divide and conquer

### 1.2 풀이과정
1. 우선 입력받은 데이터가 가공할 필요 없이 판단 가능한지 조사한다. 즉 불순물이 없는데 보석이 2개이상이거나 0개면 불가능하다,
2. 그것이 아닌경우에는 두가지 재귀호출을 한다. 0,0 ~ n,n까지 처음자르는 방향을 수직방향으로 자르는 count _
3. 0,0 ~ n,n까지 처음자르는 방향을 수평방향으로 자르는 count 이 두개를 더하는 큰 틀이다.
4. 그 안에 세부적인 내부 구현은 호출로 얻게되는 범위 내에서 총 3가지 경우를 나눈다.
5. 1) 잘랐는데 불순물이 없는부분이 생기고 보석이 1개이상이거나 0개인경우 이경우는 더이상 볼 필요 없으므로 더이상 재귀호출을 하지
6. 않도록 한다.
7. 2) 잘랐는데 아직 그 부분에는 불순물이 남아있다면 그 불순물 기준으로 또다시 재귀호출을 할 수 있도록 한다
8. 3) 잘랐는데 불순물이 없고 마침 그 안에는 보석이 한개밖에 없게 된다면 그 경우는 1을 return할 수 있도록 한다.
9. 위의 과정을 거치면서 지금 자른방법 기준으로 가능한 방법의 count가 return되고 이것을 반환할 수 있도록 설계하였다.

### 1.3 소스코드

```python
import sys

def divide (start_row, start_col, finish_row, finish_col, horizonal):
    divide_complete ,jewel, trash =0,0,0
    for i in range(start_row,finish_row):
        for j in range(start_col, finish_col):
            if arr[i][j] == 1:
                trash += 1
                if horizonal:
                    for t in range(start_col,finish_col):
                        if arr[i][t]==2:
                            break
                    else:
                        divide_complete += divide(start_row,start_col, i,finish_col, not(horizonal)) * divide(i+1,start_col,finish_row,finish_col,not(horizonal))
                else:
                    for t in range(start_row,finish_row):
                        if arr[t][j] == 2:
                            break
                    else:
                        divide_complete += divide(start_row,start_col, finish_row,j,not(horizonal)) * divide(start_row,j+1,finish_row,finish_col, not(horizonal))
            elif arr[i][j] == 2:
                jewel+=1
    if trash == 0:
        if jewel == 1:
            return 1
        else:
            return 0
    return divide_complete
n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

trash = 0
jewel = 0


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            trash += 1

        elif arr[i][j] == 2:
            jewel += 1

if trash == 0: 
    if jewel == 1:
        print(0)
    else:
        print(-1)
    sys.exit()
cnt = divide(0,0,n,n,0) + divide(0,0,n,n,1)
if cnt :
    print(cnt)
else:
    print(-1)

```





![KakaoTalk_20210929_233119676](https://user-images.githubusercontent.com/69501435/135290003-77a90f7b-8e91-4c44-ae96-e3a4900e8c94.jpg)
