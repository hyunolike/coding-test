N,M,x,y,K=map(int,input().split())

grid=[ list(map(int,input().split())) for _ in range(N) ]

command=list(map(int,input().split()))

dice=[0,0,0,0,0,0]

def rotate(direction):
    if direction==4:
        temp = dice[1:4]+dice[0:1]+dice[4:]
    elif direction==3:
        temp=dice[3:4]+dice[0:3]+dice[4:]
    elif direction==2:
        temp=dice[0:1]+dice[4:5]+dice[2:3]+dice[5:]+dice[3:4]+dice[1:2]
    elif direction==1:
        temp=dice[0:1]+dice[5:]+dice[2:3]+dice[4:5]+dice[1:2]+dice[3:4]
    
    return temp

for i in range(K):
    if command[i]==4:
        x+=1
    elif command[i]==3:
        x-=1
    elif command[i]==2:
        y-=1
    elif command[i]==1:
        y+=1
        

    if 0<=x<N and 0<=y<M:
        dice = rotate(command[i])
        if grid[x][y]==0:
            grid[x][y]=dice[1]
            print(dice[3])
        else:
            dice[1]=grid[x][y]
            grid[x][y]=0
            print(dice[3])

    else:
       # print('벗어남',x,y)
        if command[i]==4:
            x-=1
        elif command[i]==3:
            x+=1
        elif command[i]==2:
            y+=1
        elif command[i]==1:
            y-=1
