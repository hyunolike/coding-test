N,e,w,s,n = map(int, input().split())


percent = [e/100,w/100,s/100,n/100]
Map = [[0 for i in range(N*2+1)] for ii in range(N*2+1)]

dirX = [1,-1,0,0]
dirY = [0,0,-1,1]

def func1(count, x,y):
    if count==N:
        return 1
    Map[x][y] = 1 #방문표시
    ret = 0
    for i in range(4):
        X = x+dirX[i]
        Y = y+dirY[i]
        if Map[X][Y]: #방문하였다면 무시하고 진행
            continue
        ret += func1(count+1,X,Y)*percent[i] #퍼센티지 곱해주기
    Map[x][y] = 0 #이렇게 해당 경우의 수를 다 조사한뒤에는 방문한 지점을 지워줘야합니다.
    return ret

print(func1(0,N,N))