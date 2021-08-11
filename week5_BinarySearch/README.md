## [1.1477 휴게소 세우기 ](https://www.acmicpc.net/problem/1477)

![a123d](https://user-images.githubusercontent.com/87264787/129000365-8b1429cf-7668-4b05-a4b0-2b50bf08689a.png)

### 1.1 풀이 과정

1.  M개의 휴게소를 짓소 휴게소사이의 거리의 최댓값이 최소값을 구해야함

1.  휴게소사이의 거리를 중점으로 이분탐색을 해야  휴게소 간거리의 최댓값의 최소값을 구할수있음

1.  따라서 이분탐색의 시작과 끝을 고속도로의 시작과 끝으로 설정

1.  그이후 휴게소 사이에 새로운 휴게소를 지을때 특정 거리(mid)로 지었을때의 휴게소 갯수를 count헤줌

1. 이때 우리가원하는 것보다 클경우(count>M) mid값을 줄여주고 그역은 그반대로 해준다

1.이때 우리가 이분탐색끝나기 직전 거리를 늘리려고 할때가 답이 된다



### 1.2 자료구조

1.  이진 탐색(binary search) = 작은 입력 사례로 전체 입력사례의 답을 구함

1.  문제에 주어진 특별한 상황을 이해하고 활용해야함

### 1.3 소스 코드

```python

# 1477 휴게소 세우기


#문제풀이 : 1.휴게소가 없는 구간의 쵯댓값의 최솟값을 구해야함
#2. 휴게소를 한개씩 설치하는 것이아니라 한번에 M개설치하는 것이기때문에
#휴게소 사이의 거리를 기준으로 휴게소설치갯수를 이분탐색하면
#우리가 원하는 갯수의 휴게소를 휴게소간의 구간의 최대값의 최소를 구할수있따.


import sys
input = sys.stdin.readline

N , M , L = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
arr.append(0)
arr.append(L-1)
arr = sorted(arr)
#휴게소 양끝에는 설치할수없으므로 추가 + 정렬해주기

start , end = 0 , L-1

while start <= end:
    mid = (start + end) // 2
    count =0
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > mid:
            count += (arr[i] - arr[i-1] -1) // mid #/ -1은 같은자리에 지을 수 없으므로 빼줌
#특정구간의 휴게소가 몇개 설치할수 있는지 count를 통해 구해줌 
    if count > M:
        start = mid+1
    else:
        ans = mid
        end = mid -1  #정답은 휴게소갯수가 우리가 원하는 것보다
        # 많아질경우 그 전경우가 우리의 답이된다.
print(ans)


```


### 1.4 한줄평

- 이진 탐색 활용(Binary Search) ->작은 입럭사례 로 전체 입력사례의 답 구하기

-  N이 많은 문제에 최댓값,최소값을 구할때에는 이진 탐색 생각해보기
