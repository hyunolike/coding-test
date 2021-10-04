n, s = map(int, input().split())
a = list(map(int, input().split()))
answer = 1e6
left = 0
total = 0
length = 0

for i in range(len(a)):
    total += a[i]
    length += 1
    while total >= s:
        if total >= s:
            answer = min(answer, length)
        total -= a[left]
        left += 1
        length -= 1
if answer == 1e6:
    answer = 0
print(answer)