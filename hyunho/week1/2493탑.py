# 단순하게 반복문을 이용해서 풀었지만 시간 초과 ㅠ,ㅠ

num = int(input())

answer = list(map(int, input().split()))
result = []


for i in range(num-1, 0, -1):
    for j in range(i-1, 0, -1):
        if answer[i] < answer[j]:
            result.append(j+1)
            break

plus_zero = num - len(result)

for _ in range(plus_zero):
    result.append(0)

print(result[::-1])



# 스택을 최대한 이용해서 시간 초과 개선

N = int(input())
tower_list = list(map(int, input().split()))
result = [0 for _ in range(N)]
stack = []

for i in range(len(tower_list)-1, -1, -1):
    if len(stack) == 0:
        stack.append([i, tower_list[i]])

    else:
        while tower_list[i] > stack[len(stack)-1][1]: # 참일때만 while 문 수행
            tower = stack.pop() # tower 변수 .pop() 변수로 초기화 진행 tower = [4,4]
            result[tower[0]] = i+1 # result[4] = 4 거꾸로 삽입하기 위한 코드
            if len(stack) == 0:
                break

        stack.append([i,tower_list[i]])

for num in result:
    print(num, end=" ")
