from itertools import permutations

t = int(input())
nums = list(map(int, input().split()))
opcnt = list(map(int, input().split()))
op = ['+','-','*','/']
oplist = []

for i in range(4):
    for j in range(opcnt[i]):
        oplist.append(op[i])

oplist = list(set(permutations(oplist, len(oplist))))
answer = []
for case in oplist:
    n = nums[0]
    for j in range(len(nums)-1):
        if case[j]=='+':
            n += nums[j+1]
        elif case[j]=='-':
            n -= nums[j+1]
        elif case[j]=='*':
            n *= nums[j+1]
        else:
            if n//nums[j+1]<0:
                n = -(-n//nums[j+1])
            else:
                n = n//nums[j+1]
    answer.append(n)
print(max(answer))
print(min(answer))