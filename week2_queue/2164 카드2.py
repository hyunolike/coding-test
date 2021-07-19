from collections import deque

def first(n):
    queue = deque(list(i for i in range(1,n+1)))
    
    while len(queue)!=1:
        queue.popleft()
        queue.append(queue.popleft())  
    print(queue[0])

n = int(input())
first(n)


