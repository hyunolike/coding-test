import sys
input=sys.stdin.readline
N=int(input())
card=list(map(int,input().split()))

sum1,sum2=0,0
s1,s2=[0],[0]
for i in range(N):
    if i%2 == 0:
        sum1+=card[i]
        s1.append(sum1)
        s2.append(s2[-1])
    else:
        sum2+=card[i]
        s2.append(sum2)
        s1.append(s1[-1])

print(s1)
print(s2)
ans = -sys.maxsize
for i in range(N):
    if i%2==0:
        temp=s2[N-1]-s2[i-1]+s1[i-1]
        print(temp,i)
    else:
        temp= s2[i]+s1[N]-s1[i+1]+card[-1]
        print(temp,i)
    ans=max(temp,ans)
print(ans)

#odd=s2

# 1 2 3 4 5 6
# 6 2 4       :0
# 1 3 5

# 1 2 4       :1
# 6 3 5

# 1 6 4       :2
# 2 3 5

# 1 3 4       :3
# 2 6 5

# 1 3 6       :4
# 2 4 5

# 1 3 5       :5
# 2 4 6



# 6
# 1 2 3 4 5 6