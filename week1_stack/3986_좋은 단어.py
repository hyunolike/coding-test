import sys

def first(data):
    '''
        Notes:
            1. stack이 차있고, top이 ch와 같다면 pop
            2. 아니라면 stack에 push
    '''
    answer = 0
    for word in data:
        stack=[]
        for ch in word:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        if not stack:
            answer += 1
    print(answer)

n = int(input())
data = [sys.stdin.readline().strip() for i in range(n)]
first(data)
