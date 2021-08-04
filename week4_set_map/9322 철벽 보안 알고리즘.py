import sys

n = int(input())
for _ in range(n):
    m = int(input())
    data = list(input().split() for _ in range(3))
    public_key = dict()
    orders = []
    result = dict()

    for i, d in enumerate(data[0]):
        public_key[d] = i
    
    for d in data[1]:
        orders.append(public_key[d])
    
    for i, d in enumerate(data[2]):
        result[orders[i]] = d

    for i in range(m):
        if i != m-1:
            print(result[i], end=' ')
        else:
            print(result[i])
