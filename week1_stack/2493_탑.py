'''
    Notes:
        1. stack이 비어있다면 0 출력, 탑 push
        2. stack이 차 있다면 탑보다 작은 값을 모두 빼낸다.
        3. 빼낸 후 stack이 비어있다면 0 출력, 탑 push
        4. 빼낸 후 stack이 차 있다면 index 출력, 탑 push
'''
from collections import deque

def third(data):
    stack = deque()
    answer = deque()
    for i, top in enumerate(data, start=1):
        if not stack:
            answer.append(0)
            stack.append((top, i))
        else:
            while stack and stack[-1][0]<top:
                stack.pop()
            if not stack:
                answer.append(0)
                stack.append((top, i))
            else:
                answer.append(stack[-1][1])
                stack.append((top, i))
    for a in answer:
        print(a, end=' ')

def second(data):
    stack = deque()
    answer = deque()
    for i, top in enumerate(data, start=1):
        if not stack:
            answer.append(0)
            stack.append((top, i))
        elif stack and stack[-1][0]>=top:
            answer.append(stack[-1][1])
            stack.append((top, i))
        elif stack and stack[-1][0]<top:
            while stack and stack[-1][0]<top:
                stack.pop()
            if not stack:
                answer.append(0)
                stack.append((top, i))
            else:
                answer.append(stack[-1][1])
                stack.append((top, i))
    for a in answer:
        print(a, end=' ')

def first(data):
    answer = [0]
    for i in range(1, len(data)):
        for j in range(i-1, -1, -1):
            if data[i] <= data[j]:
                answer.append(j+1)
                break
            elif j == 0 and data[i] > data[j]:
                answer.append(0)

    for a in answer:
        print(a, end=' ')

n = int(input())
data = list(map(int, input().split()))
third(data)