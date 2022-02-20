# sudoku=[list(map(int,input().split())) for _ in range(9)]

# import sys
# sys.setrecursionlimit(10000000)
# def dfs(a,b):
#     global visit1
#     global visit2
#     global visit3
#     if len(visit1)==8:
#         print(visit1)
#         return
#     for i in range(9):
#         if sudoku[i][a]!=0:
#             visit1.append(sudoku[i][a])
#             dfs(i,a)
#             visit1.pop(sudoku[i][a])

# for a in range(9):
#     for b in range(9):
#         if sudoku[a][b]==0:
#             visit1=[x for x in range(1,10)]
#             visit2=[x for x in range(1,10)]
#             visit3=[x for x in range(1,10)]
#             dfs(a,b)


'포기'