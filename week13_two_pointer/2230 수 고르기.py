import sys
input = sys.stdin.readline

n,m=map(int,input().split())
a=list(int(input()) for _ in range(n))
a.sort()
answer=2e9
l,r=0,1

while True:
    if l>=n or r>=n:
        break
    diff=a[r]-a[l]
    if diff>=m:
        answer=min(answer,diff)
        l+=1
    else:
        r+=1
print(answer)

# n,m = map(int, input().split())
# a = list(int(input()) for _ in range(n))
# answer = 2e9
# l, r = 0, 1
# diff = 0
# a.sort()

# while True:
#     if l >= n or r >= n:
#         break
#     diff = a[r]-a[l]
#     if diff < m:
#         r += 1
#         continue
#     elif diff == m:
#         answer = diff
#         break
#     answer = min(answer, diff)
#     l += 1

# print(answer)