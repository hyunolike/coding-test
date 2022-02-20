N,K=map(int,input().split())

height=list(map(int,input().split()))


dif=[]
for i in range(0,N-1):
    dif.append( height[i+1]-height[i]  )
dif.sort(reverse=True)
#print(dif)
print(sum(dif[K-1:]))