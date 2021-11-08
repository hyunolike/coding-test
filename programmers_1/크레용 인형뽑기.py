from collections import deque

def solution(board, moves):
    answer = 0
    stack = deque()
    moves = deque(moves)

    while moves:
        idx = moves.popleft() - 1
        for i in range(len(board)):
            if board[i][idx]:
                stack.append(board[i][idx])
                board[i][idx] = 0
                break
        
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2

    return answer

def solution(board, moves):
    answer = 0
    moves=[m-1 for m in moves]
    stack=[]
    for m in moves:
        for i in range(len(board)):
            if board[i][m]!=0:
                stack.append(board[i][m])
                board[i][m]=0
                break
        if len(stack)>=2:
            if stack[-1]==stack[-2]:
                stack.pop()
                stack.pop()
                answer+=2
    return answer

