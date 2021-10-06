# [13주] [Two Pointer] 발표자료
1. [16161 가장 긴 증가하는 팰린드롬 부분수열](#1-1661-가장-긴-증가하는-팰린드롬-부분수열)

## 1. [16161 가장 긴 증가하는 팰린드롬 부분수열](https://www.acmicpc.net/problem/16161)

![2021-10-06](https://user-images.githubusercontent.com/69501435/136143573-2b5477ff-44bc-4067-8296-6456586b3f7b.png)

### 1.1 자료구조
1. Two pointer

### 1.2 풀이과정
1. 총 3가지 포인터를 지정했다. first, second, third 리스트를 순회하며 계속 비교해가며 그에 해당되는 작업을 할 수 있도록 하였다


### 1.3 소스코드

```python
import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

if n == 1:
    print(1)
    sys.exit()
elif n == 2:   
    if arr[0] == arr[1]:
        print(2)
        sys.exit()
    else:
        print(1)
        sys.exit()
elif n == 3:
    if arr[1]==arr[2]:
        print(2)
        sys.exit()
    

first = 0
second = 1
third = 2

max_len = 0
while first < n -2:
    if arr[first] == arr[second]:
        first-=1
        second -=1
        max_len = max(max_len,2)
        while first>=0 and third<n:
            if arr[first] == arr[third] and arr[first]<arr[second]:
                first-=1
                second-=1
                third+=1
            else:
                break
        max_len = max(max_len,third - first - 1)
        if third - second == 2:
            third+=1
        second = third-1
        first = third-2
        
    elif arr[first] == arr[third]:
        if arr[second]>arr[first]:
            max_len = max(max_len,3)
            while first>=0 and third<n:
                if arr[first] == arr[third] and arr[first]<arr[second]:
                    first-=1
                    second-=1
                    third+=1
                else:
                    break
            max_len = max(max_len,third - first -1)
            first = third-2
            second = third -1
        else:
            first+=1
            second+=1
            third+=1

    else:
        first+=1
        second+=1
        third+=1

if arr[n-1]==arr[n-2]:
    max_len = max(max_len,2)
max_len = max(max_len,1)
print(max_len)

```
![과정](https://user-images.githubusercontent.com/69501435/136144922-d2ce0655-4179-4182-97af-ebdae43a15c6.jpg)
