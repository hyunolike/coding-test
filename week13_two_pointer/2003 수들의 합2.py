n, m = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

# m보다 커지면 left를 하나 증가, 작으면 right 하나 증가
left,total=0,0
for i in range(len(a)):
    total+=a[i]
    while total>=m:
        if total==m:
            answer += 1
        total -= a[left]
        left+=1
print(answer)