# 1477 휴게소 세우기


#문제풀이 : 1.휴게소가 없는 구간의 쵯댓값의 최솟값을 구해야함
#2. 휴게소를 한개씩 설치하는 것이아니라 한번에 M개설치하는 것이기때문에
#휴게소 사이의 거리를 기준으로 휴게소설치갯수를 이분탐색하면
#우리가 원하는 갯수의 휴게소를 휴게소간의 구간의 최대값의 최소를 구할수있따.


import sys
input = sys.stdin.readline

N , M , L = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
arr.append(0)
arr.append(L-1)
arr = sorted(arr)
#휴게소 양끝에는 설치할수없으므로 추가 + 정렬해주기

start , end = 0 , L-1

while start <= end:
    mid = (start + end) // 2
    count =0
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > mid:
            count += (arr[i] - arr[i-1] -1) // mid #/ -1은 같은자리에 지을 수 없으므로 빼줌
#특정구간의 휴게소가 몇개 설치할수 있는지 count를 통해 구해줌 
    if count > M:
        start = mid+1
    else:
        ans = mid
        end = mid -1  #정답은 휴게소갯수가 우리가 원하는 것보다
        # 많아질경우 그 전경우가 우리의 답이된다.
print(ans)