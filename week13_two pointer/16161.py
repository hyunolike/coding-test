import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

if n == 1:
    print(1)
    sys.exit()
elif n == 2:   
    if arr[0] == arr[1]:
        print(2)
        sys.exit()
    else:
        print(1)
        sys.exit()
elif n == 3:
    if arr[1]==arr[2]:
        print(2)
        sys.exit()
    

first = 0
second = 1
third = 2

max_len = 0
while first < n -2:
    if arr[first] == arr[second]:
        first-=1
        second -=1
        max_len = max(max_len,2)
        while first>=0 and third<n:
            if arr[first] == arr[third] and arr[first]<arr[second]:
                first-=1
                second-=1
                third+=1
            else:
                break
        max_len = max(max_len,third - first - 1)
        if third - second == 2:
            third+=1
        second = third-1
        first = third-2
        
    elif arr[first] == arr[third]:
        if arr[second]>arr[first]:
            max_len = max(max_len,3)
            while first>=0 and third<n:
                if arr[first] == arr[third] and arr[first]<arr[second]:
                    first-=1
                    second-=1
                    third+=1
                else:
                    break
            max_len = max(max_len,third - first -1)
            first = third-2
            second = third -1
        else:
            first+=1
            second+=1
            third+=1

    else:
        first+=1
        second+=1
        third+=1

if arr[n-1]==arr[n-2]:
    max_len = max(max_len,2)
max_len = max(max_len,1)
print(max_len)