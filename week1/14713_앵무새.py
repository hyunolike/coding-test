from collections import deque

def first(n, s, l):
    for word in l:
        check = False
        for bird in s:
            if bird and bird[0] == word:
                check = True
                bird.popleft()
                break
        if not check:
            print('Impossible')
            return 0
    # 반드시 모든 단어를 받아 적어야함
    for bird in s:
        if bird:
            print('Impossible')
            return 0
    print('Possible')

n = int(input())
s = []
for i in range(n):
    tmp = list(input().split())
    tmp = deque(tmp)
    s.append(tmp)
l = list(input().split())
first(n, s, l)