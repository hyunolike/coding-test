from collections import deque

def solution(priorities, location):
    '''

    Notes:
        1. priorities의 0번째보다 더 큰 값이 있는지 확인한다.
        2. 더 큰 값이 있다면 0번째값을 맨 뒤로 보낸다.
        3. 더 큰 값이 없다면 해당 값을 출력한다.
    
    Args:
        priorities (list): 우선순위(int)를 담은 리스트
        location (int): 출력 순번을 알고 싶은 인쇄물의 index 위치

    Returns:
        answer (int): 인쇄물의 출력 순번
    '''

    answer = 0
    priorities = [(p,i) for i,p in enumerate(priorities)]
    priorities = deque(priorities)
    check = [i for i in range(len(priorities))]
    check = deque(check)

    while priorities:
        target = priorities.popleft()

        if priorities and target[0] < max(priorities)[0]:
            priorities.append(target)
        else:
            answer += 1
            if target[1] == location:
                return answer
        
    return answer


# another solution
from collections import deque

def solution(priorities, location):
    answer = 0

    q=deque()
    for idx, p in enumerate(priorities):
        q.append((idx, p))
    
    while q:
        idx, p = q.popleft()
        flag=True
        for i in range(len(q)):
            if p < q[i][1]:
                flag=False
        if flag:
            answer+=1
            if idx == location:
                return answer
        else:
            q.append((idx, p))
    
    return answer

# another solution
from collections import deque

def solution(priorities, location):
    answer = 0

    q=deque()
    for idx, p in enumerate(priorities):
        q.append((p, idx))
    
    while q:
        p, idx = q.popleft()
        if q and p < max(q, key=lambda x:x[0])[0]:
            q.append((p, idx))
        else:
            answer+=1
            if idx==location:
                return answer