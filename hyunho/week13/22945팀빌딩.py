n=int(input())
x=list(map(int,input().split()))

left, right, ans=0, n-1, 0    
# 구간이 좁아질 수록 사이에 있는 개발자 수는 감소하지만 능력치의 최소값은 증가할 수 있다
# 따라서 구간을 좁혀가면서 팀 능력치의 최대값을 찾아내야 한다

while left+1 < right:
  ans=max(ans,(right-left-1)*min(x[left],x[right]))   # 현재 두개의 포인터가 가리키고 있는 left, right 값을 이용해 최대값을 갱신한다
  if x[left]<x[right]:    
    # 포인터의 이동으로 인해 (개발자 수)는 무조건 감소한다
    # left, right 포인터 중 더 작은 것을 가리키고 있는 포인터를 이동시키면 팀 능력치의 손실을 줄일 수 있다
    left+=1
  else: 
    right-=1
      
print(ans)
