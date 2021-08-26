import sys

def dfs(val,index,string,before='+'):
    
    if index == this_n+1:
        if val== 0:
            result.append(string)
        return
    
    
    
    dfs(val+arr[index], index+1, string+'+'+str(arr[index]))
    if before == '-':
        dfs(val + arr[index-1] - (arr[index-1] * 10 + arr[index]), index + 1,  string+' '+str(arr[index]),' ')
    elif before == '+':
        dfs(val - arr[index-1] + (arr[index-1] * 10 + arr[index]), index + 1,  string+' '+str(arr[index]),' ')
    dfs(val-arr[index], index+1, string+'-'+str(arr[index]),'-')
    
   
    
n = int(sys.stdin.readline())
real_result = []
for i in range(n):
    this_n = int(sys.stdin.readline())
    arr = list(range(this_n+1))
    prune = sum(arr)
    
    result =[]
    dfs(arr[1],2,str(arr[1]))
    real_result.append(sorted(result))

for i in real_result:
    for j in i:
        for t in j:
            print(t,end='')
        print('')
    print('')