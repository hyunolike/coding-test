test = int(input())

for _ in range(test):
    data = dict()
    n = int(input())
    cnt = 1

    for _ in range(n):
        name, kind = input().split()
        if kind not in data.keys():
            name = [name]
            data[kind] = name
        else:
            data[kind].append(name)
    for k, v in data.items(): 
        cnt *= len(v)+1
    
    print(cnt-1)