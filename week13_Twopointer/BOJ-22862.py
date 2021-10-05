"""
화) 22862 가장 긴 짝수 연속한 부분 수열(large) 

문제풀이 1: 차례차례 검토해야 하고 조건 초과시 특정 지점으로 돌아가야할때 = start,end두개의 변수를 써서
투포인터 형식으로 풀기

"""

import sys
input = sys.stdin.readline

N,K = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
st , end = 0 ,0
cnt = 0
ans = 0


while 1:
    if end >= len(arr):
        break
    # 모든 수열 다 검토시 종료
    
    if arr[end]%2==0:
        end += 1
        cnt += 1
    else:
        if K > 0 :
            K -= 1 
            end += 1
        else:
            if arr[st] %2 == 0:
                st += 1
                cnt -= 1
            else:
                st += 1
                K += 1
    ans = max(ans,cnt)
print(ans)
