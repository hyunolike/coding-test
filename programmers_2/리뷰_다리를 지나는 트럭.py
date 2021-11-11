from collections import deque

def solution(bridge_length, weight, truck_weights):
    '''
    Notes:
        1. truck_weights를 큐에 넣는다.
        2. bridge_length보다 작고, weight를 넘지 않으면 truck을 stack에 넣는다.
        3. truck은 bridge_length가 되면 stack에서 빠져나간다.
    
    Args:
        1. bridge_length (int): 다리에 올라갈 수 있는 트럭 수
        2. weight (int): 다리가 버틸 수 있는 무게
        3. truck_weights (list): 트럭 무게(int)가 담긴 리스트

    Returns:
        seconds (int): 모든 트럭이 다리를 건너는 데 걸리는 최소 시간

    '''
    truck_weights = [[truck_weight, 0] for truck_weight in truck_weights]
    truck_weights = deque(truck_weights)
    queue = deque()
    seconds = 0
    w = 0


    while truck_weights:
        seconds += 1
        if len(queue) < bridge_length and w+truck_weights[0][0] <= weight:
            truck = truck_weights.popleft()
            queue.append(truck)
            w += truck[0]

        for i in range(len(queue)):
            queue[i][1] += 1

        if queue and queue[0][1] == bridge_length:
            truck = queue.popleft()
            w -= truck[0]
        
    while queue:
        seconds += 1
        if queue[0][1] == bridge_length:
            truck = queue.popleft()
            w -= truck[0]
        
        for i in range(len(queue)):
            queue[i][1] += 1

    return seconds


# another solution
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    total=0; bridge=deque(); truck_weights=deque(truck_weights)
    
    while truck_weights:
        for i in range(len(bridge)):
            bridge[i][1]+=1
        
        if bridge and bridge[0][1]==bridge_length:
            truck,sec=bridge.popleft()
            total-=truck
            
        if len(bridge)<bridge_length and total+truck_weights[0]<=weight:
            truck=truck_weights.popleft()
            bridge.append([truck,0])
            total+=truck
            
        answer+=1
    
    while bridge:
        for i in range(len(bridge)):
            bridge[i][1]+=1
        if bridge[0][1]==bridge_length:
            bridge.popleft()
        answer+=1

    return answer