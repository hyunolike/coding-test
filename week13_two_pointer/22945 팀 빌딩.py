n = int(input())
dev = list(map(int, input().split()))

l, r = 0, n-1
total=0
answer=0
while True:
    if l >= r:
        break
    total = (r-l-1)*min(dev[l], dev[r])
    answer = max(answer, total)

    if dev[l]<dev[r]:
        l += 1
    else:
        r -= 1

print(answer)