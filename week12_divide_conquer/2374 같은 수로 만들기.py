import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
stack = []

max_num = 0

for i in range(n):
    t = int(input())
    max_num = max(max_num, t)
    if not stack:
        stack.append(t)
    else:
        if stack[-1] < t:
            cnt += t - stack[-1]
            stack.pop()
            stack.append(t)
        elif stack[-1] > t:
            stack.pop()
            stack.append(t)
    
while stack:
    num = stack[-1]
    stack.pop()
    cnt += max_num - num
    
print(cnt)


# def find(value, idx):
#     ans = idx
#     for i in range(idx+1, n):
#         if a[i] == value:
#             ans += 1
#         else:
#             break
#     return idx, ans

# def add(st, ed, cnt):
#     for i in range(st, ed+1):
#         stack.append(a[i]+cnt)

# check=0
# for i in range(n):
#     if not stack:
#         st, ed = find(a[i], i)
#         add(st, ed, 0)
#         check = ed
#     if i <= check:
#         pass
#     elif a[i] == stack[-1]:
#         st, ed = find(a[i], i)
#         add(st, ed, 0)
#         check = ed
#     elif a[i] < stack[-1]:
#         cnt = stack[-1] - a[i]
#         answer += cnt
#         st, ed = find(a[i], i)
#         add(st, ed, cnt)
#         check = ed
#     elif a[i] > stack[-1]:
#         cnt = a[i] - stack[-1]
#         answer += cnt
#         for j in range(len(stack)):
#             stack[j] += cnt
#         st, ed = find(a[i], i)
#         check = ed
#         add(st, ed, 0)
        
# print(answer)

