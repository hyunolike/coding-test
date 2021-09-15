n, l = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort()
cnt = 0

for i in range(n):
    st, ed = pool[i]
    if (ed-st) % l != 0:
        length = (ed-st)//l + 1
    else:
        length = (ed-st)//l

    cnt += length
    new_ed = st + l*length

    if (i+1) < n:
        next_st = pool[i+1][0]
        if new_ed > next_st:
            pool[i+1][0] = new_ed
print(cnt)