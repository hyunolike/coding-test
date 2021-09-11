import sys
input=sys.stdin.readline

N=int(input().rstrip())
aquarium=[ list(map(int,input().split())) for _ in range(N)]
sharkSize=2
sharkLocation=(-1,-1)

def getDistnace(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

count=0
fishList=[]
for i in range(N):
    for j in range(N):
        if 1<=aquarium[i][j]<=6:
            fishList.append((i,j,aquarium[i][j])) #인덱스, 크기
            count+=1
        elif aquarium[i][j]==9:
            sharkLocation=(i,j)
print(sharkLocation)
while count!=0 :
    dist=sys.maxsize
    for i in range(len(fishList)):
        if fishList[i][2]<sharkSize:
            dist=min(dist,getDistnace(sharkLocation[0],sharkLocation[1],fishList[i][0],fishList[i][1]))
            print(dist,fishList[i])
    print(dist)
    break


#구현중~~~

