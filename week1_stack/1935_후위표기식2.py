import sys

def solution(s, data):
    '''
        Notes:
            1. 중위 -> 후위 표기식의 반대로 접근
            2. 문자를 stack에 push
                - data의 0번째가 'A'이므로 ord('A')-ord('A')와 같이 아스키코드로 접근
            3. 연산자가 나오면 2개를 pop해서 계산
                - stack은 LIFO이므로 먼저 꺼낸 것이 뒷자리 operand
            4. 계산한 결과를 stack에 push
    '''
    stack = []
    for a in s:
        if str(a).isalpha():
            stack.append(data[ord(a)-ord('A')])
        else:
            c = stack.pop()
            b = stack.pop()
            
            if a == '*':
                stack.append(b*c)
            elif a == '/':
                stack.append(b/c)
            elif a == '+':
                stack.append(b+c)
            else:
                stack.append(b-c)
    print('{:.2f}'.format(stack[0]))

n = int(input())
s = sys.stdin.readline().strip()
data = [int(sys.stdin.readline().strip()) for i in range(n)]
solution(s, data)