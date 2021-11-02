n,k=map(int,input().split())
answer=0

while n!=1:
    if n%k==0:
        n=n//k
        answer+=1
    else:
        n-=1
        answer+=1
print(answer)

# another solution
n,k=map(int,input().split())
result=0

while n>=k:
    while n%k != 0:
        n-=1
        result+=1
    n=n//k
    result+=1

while n>1:
    n-=1
    result+=1
print(result)

# another solution
n,k=map(int, input().split())
result=0

while True:
    target=(n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n=n//k

result+=(n-1)
print(result)