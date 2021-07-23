#3 큐2

#1.디큐사용 끝..


import sys
input = sys.stdin.readline


from collections import deque

N = int(input().strip())
arr = []
ans = deque()
for i in range(N):
    arr = input().split()
    
    if arr[0] == "push":
        ans.append(arr[1])
    elif arr[0] =="pop":
        if not ans:
            print("-1")
        else:
            print(ans.popleft())
    elif arr[0] == "size":
        print(len(ans))
    elif arr[0] == "empty":
        if ans :
            print("0")
        else:
            print("1")
    elif arr[0] == "front":
        if not ans:
            print("-1")
        else:
             print(ans[0])
    elif arr[0] == "back":
        if not ans:
                print("-1")
        else:
             print(ans[-1])
