#카드 2

from collections import deque

N = int(input().strip())
list1 = deque()
for i in range(1,N+1):
    list1.append(i)
    
for j in range(N-1):
    list1.popleft()
    list1.append(list1.popleft())
    
print(list1[0])
