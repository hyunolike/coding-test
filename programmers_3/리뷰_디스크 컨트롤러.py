import heapq

def solution(jobs):
    answer,current,cnt=0,0,0
    start=-1
    heap=[]
    
    while True:
        if cnt==len(jobs):
            break
        for job in jobs:
            if start<job[0]<=current:
                heapq.heappush(heap,[job[1],job[0]])
        if len(heap)>0:
            ext,st=heapq.heappop(heap)
            start=current
            current+=ext
            answer+=current-st
            cnt+=1
        else:
            current+=1
    return answer//len(jobs)