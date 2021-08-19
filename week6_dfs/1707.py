import sys
import collections
n = int(sys.stdin.readline())
result = []
for _ in range(n):
    vertex ,edge = map(int,sys.stdin.readline().split())
    graph = dict()
    start , arrive = map(int,sys.stdin.readline().split())
    stack = collections.deque([start])
    
    chil = dict()
    flag = 1
    chil[start] = 0
    graph[start] ={arrive}
    graph[arrive] = {start}
    possible = dict()
    possible[start] = False
    possible[arrive] = True
    for _ in range(1,edge):
        start, arrive = map(int,sys.stdin.readline().split())
        try:
            graph[start].add(arrive)
        except:
            graph[start] = {arrive}
            possible[start] = True
        try:
            graph[arrive].add(start)
        except:
            graph[arrive] = {start}
            possible[arrive] = True
    while(flag):
        while(len(stack) and flag):
            where = stack.popleft()
            this_color = chil[where]
            
            for i in graph[where]:
                if possible[i]:
                    stack.append(i)
                    chil[i] = (this_color + 1)%2
                    possible[i] = False
                else:
                    if this_color == chil[i]:
                        flag = 0 
                        result.append('NO')
                        break
        if flag == 0:
            break
        this_flag = 1
        for j in possible.keys():
            if possible[j]== True:
                new_vertex = j
                this_flag = 0
                break
        
        
        if this_flag:
            result.append('YES')
            break
        else:
            stack.append(new_vertex)
            chil[new_vertex] = 0
            possible[new_vertex] = False
  

for i in result:
    print(i)