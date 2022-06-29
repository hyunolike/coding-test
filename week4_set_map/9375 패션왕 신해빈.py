from collections import defaultdict

test = int(input())

for _ in range(test):
    n = int(input())
    data = defaultdict(list)
    cnt = 1
    
    for _ in range(n):
        name, kind = input().split()
        data[kind].append(name)
    
    for k, v in data.items():
        cnt *= len(v)+1
    
    print(cnt-1)


# test = int(input())

# for _ in range(test):
#     n = int(input())
#     data = dict()
#     cnt = 1

#     for _ in range(n):
#         name, kind = input().split()
#         if kind not in data.keys():
#             name = [name]
#             data[kind] = name
#         else:
#             data[kind].append(name)
#     for k, v in data.items(): 
#         cnt *= len(v)+1
    
#     print(cnt-1)