n=int(input())
answer=0

while True:
    if n<=0:
        break
    if n%5==0:
        answer+=n//5
        break
    n-=3
    answer+=1
if answer==0:
    answer=-1
print(answer)