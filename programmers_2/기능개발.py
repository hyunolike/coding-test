from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses=deque(progresses)
    speeds=deque(speeds)
    
    while progresses:
        day=(100-progresses[0])//speeds[0] \
            if (100-progresses[0])%speeds[0]==0 else (100-progresses[0])//speeds[0]+1
        
        for i in range(len(progresses)):
            progresses[i]+=day*speeds[i]
        
        progresses.popleft(); speeds.popleft(); cnt=1
        
        while progresses:
            if progresses[0]<100:
                break
            progresses.popleft(); speeds.popleft(); cnt+=1
        answer.append(cnt)
    
    return answer