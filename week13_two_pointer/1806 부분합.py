n,m=map(int,input().split())
s=list(map(int,input().split()))
answer=1e8
l,r=0,0
total=0
length=0
while True:
    if l>=n or r>=n:
        break
    total+=s[r]
    length+=1
    r+=1
    while total >= m:
        if total >= m:
            answer = min(answer, length)
        total -= s[l]
        length-=1
        l+=1
if answer==1e8:
    answer=0
print(answer)


# n, s = map(int, input().split())
# a = list(map(int, input().split()))
# answer = 1e6
# left = 0
# total = 0
# length = 0

# for i in range(len(a)):
#     total += a[i]
#     length += 1
#     while total >= s:
#         if total >= s:
#             answer = min(answer, length)
#         total -= a[left]
#         left += 1
#         length -= 1
# if answer == 1e6:
#     answer = 0
# print(answer)