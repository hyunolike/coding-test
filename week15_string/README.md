# 문자열

1. [10809 알파벳 찾기](#1-10809-알파벳-찾기)
2. [1152 단어의 개수](#2-1152-단어의-개수)
3. [1157 단어 공부](#3-1157-단어-공부)
4. [11718 그대로 출력하기](#4-11718-그대로-출력하기)
5. [11720 숫자의 합](#5-11720-숫자의-합)
6. [11721 열 개씩 끊어 출력하기](#6-11721-열-개씩-끊어-출력하기)
7. [1316 그룹 단어 체커](#7-1316-그룹-단어-체커)
8. [2941 크로아티아 알파벳](#8-2941-크로아티아-알파벳)
9. [8958 OX퀴즈](#9-8958-OX퀴즈)
10. [9012 괄호](#10-9012-괄호)

## 1. [10809 알파벳 찾기](https://www.acmicpc.net/problem/10809)
![image](https://user-images.githubusercontent.com/44918665/139560846-5df89106-465c-4c97-a691-63dc2330505e.png)

### 1.1. 해결과정
1. a부터 z까지 word안에 존재하는 인덱스를 찾는다.
2. a부터 z까지는 ord()함수를 사용하되, 1씩 증가하며 접근한다.
3. 단어 word에 대한 알파벳 인덱스는 str.find()함수를 사용한다.

### 1.2. 소스코드
```python
word=input()
answer=[]
for i in range(ord('a'), ord('z')+1):
    alpha=chr(i)
    answer.append(word.find(alpha))
print(' '.join(map(str, answer)))
```

## 2. [1152 단어의 개수](https://www.acmicpc.net/problem/1152)
![image](https://user-images.githubusercontent.com/44918665/139561001-4b3510c7-9f28-4a20-918c-6102abdd8d10.png)

### 2.1. 해결과정
- list(input().split())함수를 이용해 input을 받고, 리스트 개수를 출력한다.

### 2.2. 소스코드
```python
ch=list(input().split())
print(len(ch))
```

## 3. [1157 단어 공부](https://www.acmicpc.net/problem/1157)
![image](https://user-images.githubusercontent.com/44918665/139561068-2a0f3011-b18d-4c02-9816-a50b2981fd66.png)

### 3.1. 해결과정
1. 대소문자를 구분하지 않으므로, 대문자로 통일한다.
2. 단어를 구성하는 알파벳을 list(set())으로 추린다.
3. 각 알파벳을 str.count()함수를 사용해 개수를 카운트한다.
4. 최대값이 1개가 아니라면 ?를 출력한다.
5. 최대값이 1개라면, 최대값을 갖는 index에 해당하는 문자를 출력한다.

### 3.2. 소스코드
```python
# https://www.byfuls.com/programming/read?id=49
inputData = input().upper()
searchKeys = list(set(inputData))
 
countArr = []
for key in searchKeys:
    countArr.append(inputData.count(key))
 
if countArr.count(max(countArr)) > 1:
    print("?")
else:
    print(searchKeys[countArr.index(max(countArr))])

""" another Solution
from collections import defaultdict
word=input().upper()
cnt_dict=defaultdict(int)

for w in word:
    cnt_dict[w]+=1

answer,value=0,0
for k,v in cnt_dict.items():
    if value<v:
        value=v
        answer=k

cnt_list=list(cnt_dict.values())
if cnt_list.count(max(cnt_list))>=2:
    answer='?'
print(answer)
"""
```

## 4. [11718 그대로 출력하기](https://www.acmicpc.net/problem/11718)
![image](https://user-images.githubusercontent.com/44918665/139562201-a387806e-cd04-478a-baad-840d7d8b584d.png)

### 4.1. 해결과정
1. 입력이 언제 끝날 지 모르기 때문에 try ~ except 구문을 사용했다.
2. 입출력을 수행하되, 예외가 발생하면 except 처리로 종료한다.

### 4.2. 소스코드
```python
while True:
    try:
        a=input()
        print(a)
    except:
        break
```

## 5. [11720 숫자의 합](https://www.acmicpc.net/problem/11720)
![image](https://user-images.githubusercontent.com/44918665/139562224-57ed726a-0d78-43fe-a91e-2b4d0470c7f0.png)

### 5.1. 해결과정
1. 공백없는 값을 한 문자씩 분리하기 위해 list(map(int, input())함수를 사용했다.
2. 최종적으로 리스트로 바꾼 뒤, sum()로 결과를 출력했다.

### 5.2. 소스코드
```python
n=int(input())
num=list(map(int, input()))
print(sum(num))
```

## 6. [11721 열 개씩 끊어 출력하기](https://www.acmicpc.net/problem/11721)
![image](https://user-images.githubusercontent.com/44918665/139562262-f1f1ca78-8c42-433c-98f2-865aa99c4f01.png)

### 6.1. 해결과정


## 7. [1316 그룹 단어 체커](https://www.acmicpc.net/problem/1316)
## 8. [2941 크로아티아 알파벳](https://www.acmicpc.net/problem/2941)
## 9. [8958 OX퀴즈](https://www.acmicpc.net/problem/8958)
## 10. [9012 괄호](https://www.acmicpc.net/problem/9012)


