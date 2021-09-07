
r,c,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(3)]

time = 0
while graph[r][c]!=k:
    if time == 101:
        break
    time += 1
    rlen = len(graph)
    clen = len(graph[0])

    if rlen>=clen:
        for i in range(rlen):
            seta = set(graph[i])
            tmp = [[value, graph[i].count(value)] for value in seta]
            tmp = sorted(tmp, key=lambda x: (x[1], x[0]))
            ttmp = []
            for t in tmp:
                ttmp.extend(t)
            graph[i]=ttmp
    else:
        for i in range(clen):
            temp = [graph[j][i] for j in range(rlen)]
            seta = set(temp)
            tmp = [[value, temp[i].count(value)] for value in seta]
            tmp = sorted(tmp, key=lambda x: (x[1],x[0]))
            ttmp = []
            for t in tmp:
                ttmp.extend(t)
            for j in range(rlen):
                graph[j][i] = ttmp[j]
    
    