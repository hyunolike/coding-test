# 처음 단순하게 풀려고 시도한 코드 --> 결과적으로 실패
import sys

count = 0
stack = []

for _ in range(int(input())):
    stack = list(sys.stdin.readline().rstrip())
    if len(stack) >= 2 and len(stack) <= 100000:
        # print(stack)
        for i in range(1, len(stack)):
            if stack.count('A') == 3 or stack.count('B') == 3: # 연속 3개가 나오면 반복 중지
                break
            else:
                if stack[i-1] == stack[i]: # AA OR BB 가 나오면 count 증가
                    count += 1
                    break

print(count)


# 스택을 이용한 코드 --> 정답 코드
import sys

count = 0

# 입력 받은 데이터의 가장 마지막 부분과 입력할 받은 부분의 데이터가 같으면 빼주면 된다
# 즉 삽입하려는 알파벳과 스택의 맨 위의 알파벳이 쌍이 이루면 스택에서 꺼내는 것!
def check(word):
    temp = []
    for i in range(len(word)):
        if temp and temp[-1] == word[i]:
            temp.pop()
        else:
            temp.append(word[i])
    if not temp:
        return True
    else:
        return False


for _ in range(int(input())):
    stack = sys.stdin.readline().rstrip()
    if check(stack):
        count += 1

print(count)