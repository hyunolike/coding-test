import sys

n = int(sys.stdin.readline())

switch = list(map(int,sys.stdin.readline().split()))
switch.insert(0,-1)
student = int(sys.stdin.readline())

command = [list(map(int,sys.stdin.readline().split())) for _ in range(student)]

for i in command:
    if i[0] == 1: #남자
        howmany = n // i[1]
        for j in range(1,howmany+1):
            switch[i[1]*j] = (switch[i[1]*j] + 1) % 2
    else: #여자
        decalcomanie = i[1]
        switch[i[1]] = (switch[i[1]] + 1) % 2
        idx = 1
        while True:
            if 1 <= i[1] - idx and i[1] + idx < n+1:
                if switch[i[1] - idx] == switch[i[1] + idx]:
                    switch[i[1] - idx] = (switch[i[1] - idx] + 1) % 2
                    switch[i[1] + idx] = switch[i[1] - idx]
                    idx += 1
                else:
                    break
            else:
                break
    
for i in range(1,n+1):
    print(switch[i],'',end='')
    if i%20 == 0:
        print('')
