from itertools import combinations

N,S=map(int,input().split())

numbers=list(map(int,input().split()))

total=sum(numbers)


c=list()
for i in range(N):
    c.append( (combinations(numbers,i+1) ))

#c1=combinations(numbers,1)
#c2=combinations(numbers,2)
#c3=combinations(numbers,3)
#c4=combinations(numbers,4)
#c5=combinations(numbers,5)

count=0
for i in c:
    for j in i:
        if sum(j)==S:
            count+=1
           
print(count)


#print(total)

#print(numbers)