n = int(input())
arr = [int(i) for i in input().split()]

h_max = sum(arr[1:]) + sum(arr[2:]) - arr[1]

# i < j < k
for i in range(3, n-1):
    h = sum(arr[1:]) + sum(arr[i:]) - arr[i-1]
    if h_max < h:
        h_max = h
        
# i < k < j
for i in range(1, n-1):
    h = sum(arr[1:i+1]) + sum(arr[i:n-1])
    if h_max < h:
        h_max = h
        
# k < i < j
for i in range(1, n-1):
    h = sum(arr[:i]) + sum(arr[:n-1]) - arr[i]
    if h_max < h:
        h_max = h
    
        
print(h_max)
