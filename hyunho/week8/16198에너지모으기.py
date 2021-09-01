def dfs(arr, _sum):
  global answer

  if len(arr) == 2:
    answer = max(answer, _sum)
    return
  
  for i in range(1, len(arr) - 1):
    new_arr = arr[:]
    del new_arr[i]
    dfs(new_arr, _sum + arr[i-1]*arr[i+1])


answer = 0
n = int(input())
arr = list(map(int, input().split()))
dfs(arr, 0)
print(answer)