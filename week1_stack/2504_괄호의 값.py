import sys

def solution(ps):
    stack = []

    for s in ps:
        if s in ['(', '[']:
            stack.append(s)
            
        elif s == ')':
            t = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if t==0 else t*2)
                    break
                elif top == '[':
                    print(0)
                    return 0
                else:
                    t += top
                 
        elif s == ']':
            t = 0
            while stack:
                top = stack.pop()
                if top=='[':
                    stack.append(3 if t==0 else t*3)
                    break
                elif top == '(':
                    print(0)
                    return 0
                else:
                    t += top
        
    print(0 if '(' in stack or '[' in stack else sum(stack))
    
ps = sys.stdin.readline().rstrip()
solution(ps)