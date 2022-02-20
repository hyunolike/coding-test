import sys
input=sys.stdin.readline
N=int(input().rstrip())
conference=[list(map(int,input().split())) for _ in range(N)]
conference.sort(key=lambda x:(x[1],x[0]))
#conference.sort(key=lambda x:x[1])
#print(conference)

res=-99
count=0
for i,j in conference:
    if i>=res:
        #print(i,res,'asdf')
        res=j
        count+=1

print(count)