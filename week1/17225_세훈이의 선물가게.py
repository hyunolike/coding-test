from collections import deque

def first(a,b,data):
    sangmin = deque()
    jisu = deque()
    sangmin_r = []
    jisu_r = []
    idx=1

    if a==b==0:
        for time, color, cnt in data:
            time = int(time)
            cnt = int(cnt)

            if color=='B':
                while cnt!=0:
                    sangmin_r.append(idx)
                    idx+=1
                    cnt-=1
            else:
                while cnt!=0:
                    jisu_r.append(idx)
                    idx+=1
                    cnt-=1
    else:
        for time, color, cnt in data:
            time = int(time)
            cnt = int(cnt)
            
            if color == 'B':
                if sangmin and sangmin[-1]+a>time:
                    while cnt!=0:
                        sangmin.append(sangmin[-1]+a)
                        cnt-=1
                else:
                    while cnt!=0:
                        sangmin.append(time)
                        time += a
                        cnt-=1
            else:
                if jisu and jisu[-1]+b>time:
                    while cnt!=0:
                        jisu.append(jisu[-1]+b)
                        cnt-=1
                else:
                    while cnt!=0:
                        jisu.append(time)
                        time += b
                        cnt-=1

        while sangmin and jisu:
            if sangmin[0] <= jisu[0]:
                sangmin.popleft()
                sangmin_r.append(idx)
                idx+=1
            else:
                jisu.popleft()
                jisu_r.append(idx)
                idx+=1
        while sangmin:
            sangmin.popleft()
            sangmin_r.append(idx)
            idx+=1
        while jisu:
            jisu.popleft()
            jisu_r.append(idx)
            idx+=1
    
    print(len(sangmin_r))
    for s in sangmin_r:
        print(s, end=' ')
    print()
    print(len(jisu_r))
    for s in jisu_r:
        print(s, end=' ')

a,b,n = map(int, input().split())
data = [input().split() for i in range(n)]
first(a,b,data)