#2110 공유기 설치

#문제풀이 : 1.입력의 갯수가 매우큼 -> 아잔 탐색 시도
#2.찾으려고 하는것 = 두 공유기 사이의 최대거리 -> 한공유기 설치후 그 좌표에서
# 최대거리 이상의 거리가 있어야 공유기 설치가능 = 이것을 파악하는게 알고리즘 구현의 포인트




import sys
input =sys.stdin.readline
#기본 입력 및 선언
N,C = map(int,input().rstrip().split())
arr = []
for i in range(N):
    arr.append(int(input()))

# 좌표계 느낌으로 언급을하였고 정렬시 min값이 확실해지므로 정렬함 !
arr =sorted(arr)
answer = 0

# start ,end 설정  ->최대거리는 1부터 가장큰값까지 의 거리 따라서 end = max(arr)
end = max(arr) -1
start = 1 

while start <= end:
    mid = (start + end) //2
    count = 1
    wifi =min(arr) +mid
    # 이전 집과 어떤 집이 최대거리 이상으로 있을시 공유기 설치가 가능하므로
    # 설치한 공유기 갯수를 +1 해주고 그위치부터 다시 공유기거리 판단
    # 따라서 특정 최대거리(mid)일때 카운트갯수를 조건으로 분할 시도!
    for i in range(1,len(arr)):
        if wifi <= arr[i]:
            count +=1
            wifi = arr[i] +mid
    # 카운트 클시 -> 거리가 작다는것이므로 거리증가
    if count >= C:
        start = mid+1
    else:
        end = mid -1
        
# 답 : 이렇게 최대거리르 탐색하다가 카운트와 일치하고 가장큰값이 최대거리가 된다.

print(end)
