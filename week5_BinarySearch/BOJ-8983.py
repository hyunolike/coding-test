#8983 사냥꾼

#문제풀이 : 1. input = 사냥꾼자리 + 동물위치 output = L범위안에 있는 동물 수
#2 . 동물의 관점에서 자기가 사냥당할수있는지 없는지 판단하는게 for문을 한번만 돌려도됨
#3. 따라서 동물에게 가장 가까운곳에 잇는 사냥꾼의 자리 2개를 가지고 비교 ->사냥꾼의자리를 이분탐색으로 구함
#4 . 한개를 가지고 비교하니 격차클경우  놓칠수 있음.


import sys
input = sys.stdin.readline

N,M,L = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
arr = sorted(arr)
ani = []
for i in range(M):
    A,B = map(int,input().rstrip().split())
    ani.append([A,B])

count = 0

# 동물 마다 체크
for i in ani:
    start = 0
    end = len(arr)-1
    #사냥꾼 위치 체크 (이분탐색)
    while start < end:
        mid = (start + end )// 2

        if arr[mid] < i[0]:
            start = mid +1
        else:
            end = mid
    # 사냥꾼 - L 거리 비교후 카운트 세주기
    if abs(arr[end]-i[0])+i[1] <=L or abs(arr[end-1]-i[0])+i[1] <= L:
        count +=1
print(count)
         
        
        

