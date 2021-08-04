test = int(input())

for _ in range(test):
    data = dict()
    n = int(input())
    cnt = 1

    for _ in range(n):
        a, b = input().split()
        if b not in data.keys():
            a = [a]
            data[b] = a
        else:
            data[b].append(a)
    for k, v in data.items(): 
        cnt *= len(v)+1
    
    print(cnt-1)