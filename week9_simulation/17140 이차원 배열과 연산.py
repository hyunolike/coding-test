import sys
from collections import Counter
r,c,k = map(int, sys.stdin.readline().split())
maps = []
for _ in range(3):
    temp = list(map(int, sys.stdin.readline().split()))
    maps.append(temp)

time=0
find=False
while time<=100:
    if r<=len(maps) and c<=len(maps[0]) and maps[r-1][c-1]==k:
        print(time)
        find=True
        break
    time+=1
    max_col=0
    next_maps=[]
    if len(maps)>=len(maps[0]):
        for rows in maps:
            next_row=[]
            count_table=sorted(list(Counter(rows).items()), key=lambda x: (x[1],x[0]))
            for num, cnt in count_table:
                if num==0:
                    continue
                next_row.append(num)
                next_row.append(cnt)
            max_col=max(max_col, len(next_row))
            next_maps.append(next_row)
        
        for rows in next_maps:
            if len(rows)<max_col:
                for _ in range(max_col-len(rows)):
                    rows.append(0)
        maps=next_maps
        continue
    
    elif len(maps)<len(maps[0]):
        maps=list(map(list, zip(*maps)))
        for rows in maps:
            next_row=[]
            count_table=sorted(list(Counter(rows).items()), key=lambda x:(x[1],x[0]))
            for num, cnt in count_table:
                if num==0:
                    continue
                next_row.append(num)
                next_row.append(cnt)
            max_col=max(max_col, len(next_row))
            next_maps.append(next_row)

        for rows in next_maps:
            if len(rows)<max_col:
                for _ in range(max_col-len(rows)):
                    rows.append(0)
        
        maps=list(map(list, zip(*next_maps)))
        continue
if not find:
    print(-1)