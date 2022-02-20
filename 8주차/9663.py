










# 문제 잘못읽고 최대 퀸 갯수 세는 프로그램 만듦ㅡㅡ
# #N=int(input())
# import copy
# N=15
# Maingrid=[ [0]*N for _ in range(N) ]

# def makeGrid(x,y):
#    # global grid
#     for iiii in range(0,N):
#         mx,my=x+iiii,y+iiii
#         if 0<=mx<N:
#             grid[mx][y]=1
#         if 0<=my<N:
#             grid[x][my]=1
#         mx,my=x-iiii,y-iiii
#         if 0<=mx<N:
#             grid[mx][y]=1
#         if 0<=my<N:
#             grid[x][my]=1
#     for iiiii in range(1,N):
#         mx,my=x+iiiii,y+iiiii
#         if 0<=mx<N and 0<=my<N:
#             grid[mx][my]=1
#         mx,my=x-iiiii,y-iiiii
#         if 0<=mx<N and 0<=my<N:
#             grid[mx][my]=1
#         mx,my=x-iiiii,y+iiiii
#         if 0<=mx<N and 0<=my<N:
#             grid[mx][my]=1
#         mx,my=x+iiiii,y-iiiii
#         if 0<=mx<N and 0<=my<N:
#             grid[mx][my]=1
#     grid[x][y]=2
#     #return grid

# def backTrack(x,y):

#     stack=[]
#     visit=[ [0]*N for _ in range(N) ]
#     makeGrid(x,y)
#     for i in range(N):
#         for j in range(N):
#             if grid[i][j]==0:
#                 grid[i][j]=2
#                 backTrack(i,j)



# result=-1
# for ii in range(N):
#     for jj in range(N):
#         grid=copy.deepcopy(Maingrid)
#         count=0
#         backTrack(ii,jj)
#         for aa in range(N):
#             for bb in range(N):
#                 if grid[aa][bb]==2:
#                     count+=1
#         result=max(result,count)

# print(result)