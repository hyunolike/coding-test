import sys

m, n = map(int,sys.stdin.readline().split())

k = int(sys.stdin.readline())

map_info = [list(map(str,sys.stdin.readline().strip())) for _ in range(m)]

lst = [list(map(lambda x : int(x)- 1,sys.stdin.readline().split())) for _ in range(k)]


info = []
for i in range(m):
    info.append([[0,0,0]])
    for j in range(n):
        if map_info[i][j] == 'J':
            info[i].append([info[i][j][0]+1,info[i][j][1],info[i][j][2]])
        elif map_info[i][j] == 'I':
            info[i].append([info[i][j][0],info[i][j][1]+1,info[i][j][2]])
        else:
            info[i].append([info[i][j][0],info[i][j][1],info[i][j][2]+1])
    del info[i][0]
for i in range(1,m):
    for j in range(n):
        info[i][j][0]= info[i-1][j][0]+info[i][j][0]
        info[i][j][1]= info[i-1][j][1]+info[i][j][1]
        info[i][j][2]= info[i-1][j][2]+info[i][j][2]

for i in lst:

    cnt_J = info[i[2]][i[3]][0]
    cnt_I = info[i[2]][i[3]][1]
    cnt_O = info[i[2]][i[3]][2]
   
    if i[0] == 0 and i[1] == 0:
        print(cnt_J,cnt_O,cnt_I)
    elif i[0] == 0 and i[1] >0 :
        cnt_J-=info[i[2]][i[1]-1][0]
        cnt_I-=info[i[2]][i[1]-1][1]
        cnt_O-=info[i[2]][i[1]-1][2]
        print(cnt_J,cnt_O,cnt_I)
    elif i[0] >0 and i[1] == 0:
        cnt_J -= info[i[0]-1][i[3]][0]
        cnt_I -= info[i[0]-1][i[3]][1]
        cnt_O -= info[i[0]-1][i[3]][2]
        print(cnt_J,cnt_O,cnt_I)
    else:
        cnt_J-=info[i[2]][i[1]-1][0] + info[i[0]-1][i[3]][0] - info[i[0]-1][i[1]-1][0]
        cnt_I-=info[i[2]][i[1]-1][1] + info[i[0]-1][i[3]][1] - info[i[0]-1][i[1]-1][1]
        cnt_O-=info[i[2]][i[1]-1][2] + info[i[0]-1][i[3]][2] - info[i[0]-1][i[1]-1][2]
        print(cnt_J,cnt_O,cnt_I)

