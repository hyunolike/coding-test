from copy import deepcopy
n,k,b = map(int, input().split())

sign=[1]*(n+1)
psum=[0]*(n+1)
sign[0]=0

for _ in range(b):
    broken = int(input())
    sign[broken]=0

psum = deepcopy(sign)

for i in range(1, n+1):
    psum[i] += psum[i-1]

answer=0
for i in range(k, n+1):
    temp = psum[i]-psum[i-k]
    if answer < temp:
        answer = temp
print(k - answer)