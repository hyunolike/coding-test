from collections import defaultdict

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    cloth = defaultdict(int)

    for _ in range(n):
        a ,b = input().split()
        cloth[b] += 1
    list_of_key = list(cloth.keys())
    list_of_value = list(cloth.values())
    if len(list_of_key) == 1:
        print(list_of_value[0])
    else:
        answer = 1
        for i in range(len(list_of_value)):
            answer *= list_of_value[i] + 1
        print(answer - 1)