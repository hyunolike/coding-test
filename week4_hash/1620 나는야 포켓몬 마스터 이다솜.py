import sys

n,m = map(int, sys.stdin.readline().strip().split())
data = dict()
rev_data = dict()
question = []
value = 0

for _ in range(n):
    key = sys.stdin.readline().strip()
    value += 1
    if key not in data.keys():
        data[key] = value
    if value not in rev_data.keys():
        rev_data[value] = key

question = list(sys.stdin.readline().strip() for _ in range(m))

for q in question:
    if q.isdigit(): # q는 str타입 : q가 숫자로만 이루어진 문자열인가?
        print(rev_data[int(q)])
    else:
        print(data[q])