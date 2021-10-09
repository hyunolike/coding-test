import sys

def recur(want):
    try:
        return dp[want]
    except:
        value = 0
        for i in range(want-1):
            value+=recur(i)
      
        dp.append(3*recur(want-1)+ 2*value)

        return dp[want]  
  
n = int(sys.stdin.readline())
dp = [1,3]
if n%2 :
    print(0)
    
else:
    recur(n//2)
    print(dp[-1])