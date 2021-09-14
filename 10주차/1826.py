import sys
input=sys.stdin.readline

N=int(input().rstrip())
station=[list(map(int,input().split())) for _ in range(N)]
station.sort(key=lambda x:x[0])
L,P=map(int,input().split())

# 포 기 는 배 추 를 셀 때 쓰 지만 코 딩 할 때도 쓴 다 !