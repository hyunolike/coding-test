import sys

def dfs(index,count,string):
    if index == length:
        if count + 1 == 6:
            result.append(string+' '+str(arr[index]))
        elif count == 6:
            result.append(string)
        return
    dfs(index+1,count+1,string+' '+str(arr[index]))
    dfs(index+1,count,string)



real_result = []
while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    length = arr[0]
    result = []
    for i in range(1,length-4):
        dfs(i+1,1,str(arr[i]))
    real_result.append(result)
for i in real_result:
    for j in i:
        string = list(j.split())
        for t in string:
            print(int(t),'',end='')
        print('')
    print('')