import sys

def energy(i):
    popped=weight[i]
    e=weight[i-1]*weight[i+1]
    weight.pop(i)
    return e,popped


def dfs(t):
    global result
    if len(weight)==2:
        result=max(t,result)
        return
    for i in range(1,len(weight)-1):
        e,popped=energy(i)
        dfs(t+e)
        weight.insert(i,popped)

result = -sys.maxsize-1
N=int(input())
weight=list(map(int,input().split()))
dfs(0)
print(result)


