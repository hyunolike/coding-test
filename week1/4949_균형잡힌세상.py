'''
    Notes:
        1. 여는 괄호가 나오면 stack에 push
        2. 닫는 괄호가 나오면 stack에서 pop
        3. stack이 비어있거나 짝이 안맞으면 no 출력
        4. 문자열이 끝났을 때 stack이 비어 있고 마지막 문자라면 yes 출력
'''

while True:
    string = input()
    stack=[]
    check=1
    if string == '.':
        break
    for s in str(string).strip():
        if s == ')':
            if not stack:
                check=0
                break
            elif stack and stack[-1]=='(':
                stack.pop()
            elif stack and stack[-1]=='[':
                check=0
                break
        elif s == ']':
            if not stack:
                check=0
                break
            elif stack and stack[-1]=='[':
                stack.pop()
            elif stack and stack[-1]=='(':
                check=0
                break
        elif s in ['(','[']:
            stack.append(s)
    if check and not stack:
        print('yes')
    else:
        print('no')