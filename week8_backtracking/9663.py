import sys


def way(row,col,goal,count):
    r = row[-1] + 1
    if r == goal:
    
        return count+1
    possible_col=[True for _ in range(goal)]
    for i in range(r):
        this_row = row[i]
        this_col = col[i]
        if this_col - (r-this_row) >=0:
            possible_col[this_col - (r - this_row)] = False 
        if this_col + (r-this_row) < goal:
            possible_col[this_col + r - this_row] = False
        possible_col[this_col] = False
    row.append(r)
    lst = [i for i in range(len(possible_col)) if possible_col[i]==True]
    if len(lst)==0:
        row.pop(-1)
        return count
    for i in lst:
        col.append(i)
        count = way(row,col,goal,count)
        col.pop(-1)
    row.pop(-1)
   
    return count



n = int(sys.stdin.readline())

count = 0
for i in range(n//2):
        up = way([0],[i],n,0)
        count+=up
count *= 2
if n%2 == 1:
    count += way([0],[n//2],n,0)
print(count)