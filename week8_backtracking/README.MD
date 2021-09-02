# [8주] [Back tracking] 발표자료
1. [2661 좋은 수열](#1-2661-좋은-수열)

## 1. [2661 좋은 수열](https://www.acmicpc.net/problem/2661)
![2021-09-01](https://user-images.githubusercontent.com/69501435/131613135-30187847-12df-4fbc-947c-5cd9376ac924.png)


### 1.1 자료구조
1. dfs (dfs function) : [최소값부터 순회하는 dfs function]

### 1.2 풀이과정
1. 우선 지금 과정에서 조사해야할 문자열의 개수를 알아본다 
2. ex) 2번째 index의 경우 1번째만 비교하면 된다.
3. ex) 6번째 index 의 경우 123 vs 456, 34 vs 56, 5 vs 6 비교를 해야한다. (인접 부분수열과 비교)
4. 특징 : 지금 조사하려는 index의 2로나눈 몫만큼의 비교가 필요!!
5. 그래서 dfs로 쭉 조사해 나가다 만약 우리가 원하는 idx까지 구하게 되는경우 출력하는 형식

### 1.3 소스코드

```python
import sys

def dfs(idx,result):
    if idx == n+1:
        for i in range(1,n+1):
            print(result[i],end='')
        sys.exit()
    compare = idx//2
    for this_turn in possible:
        flag = 1
        for i in range(compare):
            count = i + 1
            compare_idx = idx - count
            compare_string = str()
            string = this_turn
            for k in range(count):
                compare_string = compare_string + result[compare_idx - k]
            for k in range(1,count):
                string = string + result[idx - k]
            if string == compare_string:
                flag = 0
                break
        if flag:
            dfs(idx+1, result+this_turn)
        
        
n = int(sys.stdin.readline())

result ='0'

possible = ['1','2','3']

dfs(1,result)


```
