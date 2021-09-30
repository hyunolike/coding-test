import sys
input = sys.stdin.readline

n=int(input())
A,B,C,D = [],[],[],[]
for _ in range(n):
    a,b,c,d = map(int, input().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

AB, CD = {}, {}
for a in A:
    for b in B:
        # 딕셔너리 get : key에 해당하는 value 리턴, 없을 시 None
        # get(key, default) : 만약 리턴 시 None이 아닌 default 지정 가능
        AB[a+b] = AB.get(a+b, 0)+1
answer=0
for c in C:
    for d in D:
        answer += AB.get(-(c+d), 0)
print(answer)