import sys

def getParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent[x])
        return parent[x]

def unionParent(x, y):
    a = getParent(x)
    b = getParent(y)
    
    if a != b: 
        parent[b] = parent[a]
        number[a] += number[b]

n = int(input())

for _ in range(n):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = sys.stdin.readline().strip().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        unionParent(x, y)
        print(number[getParent(x)])