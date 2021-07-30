#4358 생태학

#문제풀이1. 딕셔너리 사용  2.setdefault 사용  3.출력

import sys
input = sys.stdin.readline

arr  = {}
sum = 0
while 1 :
    N = input().rstrip()
    if not N:
        break
    arr.setdefault(N,0)
    arr[N] += 1
    sum +=1

for N in sorted(arr.keys()):
    print("%s %.4f" %(N,arr[N]*100/sum))