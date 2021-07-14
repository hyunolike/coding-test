s = input()

# 우선순위 별 숫자 리턴
def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

# 스택
stack = []
result = ""

for i in s:
    if i.isalpha(): # 내장 함수 사용
        result += i
        continue

    if i == '(':
        stack.append(i)
    elif i == ')':
        while(True):
            if stack and stack[-1] != '(': 
                result += stack.pop()
            else: # ( 이거를 그냥 빼주는 거
                stack.pop()
                break
    else:
        while(True):
            if stack and (priority(stack[-1]) >= priority(i)): # 우선순위가 top이 더 높으면 그걸 빼서 리턴 그 다음에 넣자
                result += stack.pop()
            else:
                stack.append(i)
                break
while(True):
    if stack:
        result += stack.pop()
    else:
        break

print(result)