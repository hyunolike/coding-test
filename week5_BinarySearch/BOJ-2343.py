# 2343 기타레슨 

# 2343 기타레슨 

#문제풀이 1: 검사해야되는 표본수가 매우 많기 떄문에 각각 비교 불가능
# 2: 이진 탐색 사용 -> 1.start,end 결정 1.5 분할 조건 구현 2. 분할 ->불가시 종료 

import sys
input = sys.stdin.readline

# 기본 선언 및 start, end 설정
N,M = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))

start , end = max(arr) , sum(arr)


# 이진 탐색의 일반적인 종료조건
while start <= end:
    mid = (start + end) //2
    
    limit = 0
    
    div = 1
    # 이진 탐색하기 위한 분할의 조건을 구현 
    # mid 의크기를 가진 블루레이를 주어진 자료와 비교했을때 우리가 원하는
    # 블루레이 갯수와 일치하는지 비교
    for i in range(N):
        limit += arr[i]
        if limit > mid:
            div += 1
            limit = arr[i]
    # div = 블루레이 갯수 더많을시 블루레이최대크기를 증가 / 그외 반대
    if div <=M:
        answer = mid
        end = mid -1
    else:
        start = mid+1


# 딥 도출
print(answer)


