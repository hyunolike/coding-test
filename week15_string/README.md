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
1. 10개씩 끊어 출력해야 하므로, 단어를 앞에서부터 10개씩 잘랐다.
2. 자른 10개 문자를 출력하고, 만약 남은 길이가 10이하라면 반복문을 종료한다.
3. 남아 있는 문자를 출력한다.

### 6.2. 소스코드
```python
word=input()
while word:
    if len(word)<=10:
        break
    tmp=word[:10]
    word=word[10:]
    print(tmp)
print(word)
```

## 7. [1316 그룹 단어 체커](https://www.acmicpc.net/problem/1316)
![image](https://user-images.githubusercontent.com/44918665/139605144-15a7089e-1f7d-455c-948a-8f52d35665d4.png)

### 7.1. 해결과정
1. 단어를 입력받고, 이미 나온 알파벳을 저장하는 set을 생성한다.
2. i번째부터 i-1번째가 다른 값일 경우 space에 word[i]가 있는지 확인한다.
3. 이미 set에 있는 단어라면 flag를 False로 변경하고 break
4. set에 없는 단어라면 set에 추가한다.
5. flag가 True라면 개수를 1 증가시킨다.

- 1번째부터 len(word)까지 word[i] vs word[i-1]로 비교해야 하는 이유
- 0번째부터 len(word)-1까지 word[i] vs word[i+1]일 경우, i+1번째가 이미 set에 등장했던 문자일 수 있기 때문이다.

### 7.2. 소스코드
```python
n=int(input())
answer=0
for _ in range(n):
    word=input()
    space=set()
    flag=True
    for i in range(1, len(word)):
        if word[i]!=word[i-1]:
            if word[i] in space:
                flag=False
                break
            else:
                space.add(word[i-1])
    if flag:
        answer+=1
print(answer)
```

## 8. [2941 크로아티아 알파벳](https://www.acmicpc.net/problem/2941)
![image](https://user-images.githubusercontent.com/44918665/139605659-1ab46d5e-df8f-4fe8-a041-f327e9c71217.png)

### 8.1. 해결과정
1. 찾아본 좋은 풀이는 '치환'해버리는 것이다.
2. 파이썬의 replace 함수를 이용해 크로아티아 알파벳을 하나씩 꺼내가며 특정문자로 치환한다.
3. 치환한 크로아티아 알파벳의 길이를 카운트한다.

- 주의할 점은 'dz='가 'dz'보다 먼저 와야한다.
- 이유는 dz가 먼저 와버리면, dz=를 의미하는 데 잘못 치환한 것이 된다.

### 8.2. 소스코드
```python
# https://ooyoung.tistory.com/74

word=input()
answer=0
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia:
    word = word.replace(i, '*')
print(len(word))
```

## 9. [8958 OX퀴즈](https://www.acmicpc.net/problem/8958)
![image](https://user-images.githubusercontent.com/44918665/139605821-fbf84cb8-ddb9-43ee-bb32-e8ab57701ff2.png)

### 9.1. 해결과정
1. O를 만나면 score+=1을 한 뒤 total에 더한다.
2. X를 만나면 score를 0으로 초기화한다.

### 9.2. 소스코드
```python
n=int(input())
for _ in range(n):
    case=list(map(str, input()))
    score,total=0,0
    for c in case:
        if c=='O':
            score+=1
            total+=score
        else:
            score=0
    print(total)
```

## 10. [9012 괄호](https://www.acmicpc.net/problem/9012)
![Uploading image.png…]()

### 10.1. 해결과정
1. (가 나오면 stack에 넣는다.
2. )가 나오면 stack을 pop한다.
3. )가 나왔는데 stack이 비어있다면 NO를 출력하고 종료하고 flag를 False로 변경한다.
4. 위 과정을 끝낸 후, stack이 차있다면 NO를 출력하고 flag를 False로 변경한다.
5. flag가 True라면 YES를 출력한다.

### 10.2. 소스코드
```python
t=int(input())
for _ in range(t):
    word=input()
    stack=[]
    flag=True
    for w in word:
        if w=='(':
            stack.append(w)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                flag=False
                break
    if stack:
        print('NO')
        flag=False
    if flag:
        print('YES')
```


