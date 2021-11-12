import heapq

def solution(operations):
    answer = []
    
    maxh,minh=[],[]
    
    for op in operations:
        a,n=op.split()
        if a=='I':
            heapq.heappush(maxh, -int(n))
            heapq.heappush(minh, int(n))
        elif a=='D' and n=='1' and maxh:
            num=-1*heapq.heappop(maxh)
            minh=[m for m in minh if m!=num]
            heapq.heapify(minh)
        elif a=='D' and n=='-1' and minh:
            num=heapq.heappop(minh)
            maxh=[-m for m in minh if -m!=num]
            heapq.heapify(maxh)
            
    if len(maxh)==len(minh)==0:
        answer=[0,0]
    else:
        answer.append(-heapq.heappop(maxh))
        answer.append(heapq.heappop(minh))
            
    return answer