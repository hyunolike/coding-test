import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().rstrip()
    flag = False # true이면 vps가 아님
    stack = []
    for i in range(len(s)):
        if s[i] == '(': #여는 괄호면 스택에 넣기
            stack.append(s[i])
        else:
            #닫는 괄호면 pop해서 여는 괄호와 짝인지
            #빈 스택이면 여는 괄호가 없으므로
            if len(stack) == 0 or stack.pop() != '(':
                flag = True
                break

    if flag or len(stack) != 0: #중간에 종료되거나, 여는 괄호가 남아있을 때
        print('NO')
    else:
        print('YES')

'''
vps가 되려면
 1. '('와 ')'의 개수가 같아야
 2. '('이 ')'보다 먼저 나와야
'''