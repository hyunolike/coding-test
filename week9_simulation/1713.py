import sys
import collections
n = int(sys.stdin.readline())

count = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

title = [0] * n

vote = [0] * 101

long = 0

stack = collections.deque([])

for i in arr:
    vote[i] += 1
    flag = 0
    if i in title:
        continue
    for j in range(n):
        if not title[j]:
            flag = 1
            break
    if flag:
        title[j] = i
    else:
       
        min_vote = 1000
        for j in range(n):
            if min_vote > vote[title[j]]:
                stack.clear()
                stack.append(j)
                min_vote = vote[title[j]]
                
        have_to_expire = stack.pop()
        vote[title[have_to_expire]] = 0
        del title[have_to_expire]
        
        title.append(i)
    
title.sort()

for i in title:
    if i:
        print(i,'',end='')
            
