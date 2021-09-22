# week11 발표자료

## 1. 20438 출석체크

### 1.1 자료구조

   
### 1.2 풀이과정 
- 출석 코드들 중 졸고 있는 학생들을 제외

✅ 학생 출석 코드 삽입 로직
- for문을 입장 번호의 배수만큼 건너뛰면서 반복 진행 
  - 졸고 있는 학생이 아니면 참석 가능 집합에 추가

✅ 해시테이블 로직 적용
- 특정 구간의 입장 번호 받은 학생 추가

### 1.3 소스코드

```python
import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

students = [0]*(n+3) # 해당 0인덱스 제외하기 위해 n+2+1 = n+3
sleep = set(map(int, input().split())) # k명의 졸고 있는 학생의 입장 번호들
attend = list(map(int, input().split())) # 출석 코드를 받을 학생의 입장 번호들
attendPossible = set() 

for code in attend:
    if code in sleep:
        continue
    for ncode in range(code, n+3, code):
        if ncode not in sleep:
            attendPossible.add(ncode)
            
for i in range(3, n+3): # 해시테이블 로직 적용
    students[i] += students[i-1] # 학생 추가
    if i in attendPossible: 
        students[i] += 1 

for _ in range(m):
    s, e = map(int, input().split())
    print((e-s+1)-(students[e]-students[s-1]))
```
