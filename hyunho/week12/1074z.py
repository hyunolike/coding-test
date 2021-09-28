n, r, c = map(int, input().split())

num = 0

while n > 1:
    # 4등분 중 몇번째인가
    ran = 2 ** (n - 1)
    if r >= ran:
        if c >= ran: # 4번째
            num += (4 ** (n - 1)) * 3
            r -= ran
            c -= ran
        else: # 3번째
            num += (4 ** (n - 1)) * 2
            r -= ran
            
    else:
        if c >= ran: # 2번째
            num += (4 ** (n - 1)) * 1
            c -= ran
        else: # 1번째
            pass
    
    # print(num, r, c)
    n -= 1

if r == 0:
    if c == 0:
        print(num)
    else:
        print(num + 1)
else:
    if c == 0:
        print(num + 2)
    else:
        print(num + 3)
