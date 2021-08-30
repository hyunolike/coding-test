
import copy
n,E,W,N,S=map(int,input().split())

def dfs(X,Y):






direction=['E','W','N','S']
grid=[ [0]*29 for _ in range(29) ]
dfs()
prob=0
for i in result:
    temp=1
    for j in i:
        if j=='E':
            temp*=E/100
        elif j=='W':
            temp*=W/100
        elif j=='N':
            temp*=N/100
        elif j=='S':
            temp*=S/100
    prob+=temp
print(prob)


# def isMad(direct):
#     grid=[ [0]*29 for _ in range(29) ]
#     tempX,tempY=14,14
#     grid[tempX][tempY]=1
#     for i in direct:
#         if i=='E':
#             if grid[tempX][tempY+1]==1:
#                 return False
#             else:
#                 grid[tempX][tempY+1]=1
#                 tempY+=1
#         elif i=='W':
#             if grid[tempX][tempY-1]==1:
#                 return False
#             else:
#                 grid[tempX][tempY-1]=1
#                 tempY-=1
#         elif i=='N':
#             if grid[tempX-1][tempY]==1:
#                 return False
#             else:
#                 grid[tempX-1][tempY]=1
#                 tempX-=1
#         elif i=='S':
#             if grid[tempX+1][tempY]==1:
#                 return False
#             else:
#                 grid[tempX+1][tempY]=1
#                 tempX+=1
#     return True    
