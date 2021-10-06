import sys
input = sys.stdin.readline

n,k=map(int, input().split())
brick=list(map(int, input().split()))
l, r = 0, 0
answer, cnt = 1,1
jump=1
while True:
    if l >= n-1 or r >= n-1:
        break
    if brick[r]<=k:
        cnt += 1
        r += 1
    elif brick[r]>k:
        if jump:
            jump -= 1
            cnt += 1
            r += 1
        else:
            while brick[l]<=k:
                l += 1
                cnt -= 1
            if brick[l]>k:
                l += 1
                cnt -= 1
            r += 1
            cnt += 1
    answer = max(answer, cnt)
print(answer)

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# brick = list(map(int, input().split()))
# idx = 0
# answer = 1

# for j in range(len(brick)):
#     chance = True
#     lcnt = 1
#     for i in range(j, len(brick)):
#         if k < brick[i] and not chance:
#             idx = i
#             break
#         elif k < brick[i] and chance:
#             chance = False
#             lcnt += 1
#         elif k >= brick[i]:
#             lcnt += 1
    
#     answer = max(answer, lcnt)

# print(answer)