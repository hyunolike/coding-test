import sys
import operator

k, l = map(int, input().split())
success = dict()
order = 1

for _ in range(l):
    student = sys.stdin.readline().strip()
    success[student] = order
    order += 1

success = sorted(success.items(), key = operator.itemgetter(1))

cnt = 0
for key, value in success:
    if cnt == k:
        break
    print(key)
    cnt+=1