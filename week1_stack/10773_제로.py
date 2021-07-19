import sys

def solution(data):
    '''
        Notes:
            1. 0일 경우와 아닐 경우 구분
            2. 0이 아닐 경우 stack에 push
            3. 0일 경우 stack에서 pop 
    '''
    stack=[]
    for d in data:
        if d != 0:
            stack.append(d)
        else:
            stack.pop()
    
    answer = sum(stack)
    return answer

k = int(input())
data = [int(sys.stdin.readline().strip()) for i in range(k)]
print(solution(data))
