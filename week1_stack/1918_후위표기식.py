import sys

def solution(s):
    '''
        Notes:
            1. 문자는 그대로 적는다.
            2. 연산자, (가 나오면 스택에 push
            3. top보다 우선순위가 같거나 낮은 연산자가 들어왔을 경우 pop
            4. )가 나올 경우 (를 만날때까지 pop
    '''

    answer = ''
    stack = []
    for a in s:
        if a == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        elif a in ['*','/']:
            while stack and stack[-1]!='(':
                if stack[-1] in ['*','/']:
                    answer += stack.pop()
                else:
                    break
            stack.append(a)
        elif a in ['+','-']:
            while stack and stack[-1]!='(':
                answer += stack.pop()
            stack.append(a)
        elif a == '(':
            stack.append(a)
        else:
            answer += a

    while stack:
        answer += stack.pop()
    print(answer)


def best_solution(exp):
    answer = ''
    stack = []

    for e in exp:
        if e == '(':
            stack.append(e)
        elif e == ')':
            while stack and stack[-1]!='(':
                answer += stack.pop()
            stack.pop()
        elif e in ['+','-']:
            while stack and stack[-1] in ['+','-','*','/']:
                top = stack.pop()
                answer += top
            stack.append(e)
        elif e in ['*','/']:
            while stack and stack[-1] in ['*','/']:
                top = stack.pop()
                answer += top
            stack.append(e)
        else:
            answer += e
        
    while stack:
        top = stack.pop()
        if top != '(':
            answer += top
    print(answer)

s = sys.stdin.readline().strip()
solution(s)