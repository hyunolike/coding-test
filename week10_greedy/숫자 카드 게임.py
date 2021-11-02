n,m=map(int, input().split())
card=[list(map(int, input().split())) for _ in range(n)]
value=[]
for c in card:
    value.append(min(c))
print(max(value))

# another solution
n,m=map(int, input().split())

result=0
for i in range(n):
    data=list(map(int, input().split()))
    min_value=min(data)
    result=max(result, min_value)

print(result)

# another solution
n,m=map(int, input().split())

result=0
for i in range(n):
    data=list(map(int, input().split()))
    min_value=10001
    for a in data:
        min_value=min(min_value, a)
    result=max(result, min_value)
    
print(result)