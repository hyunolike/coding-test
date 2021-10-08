import sys

def bsearch(left,right,value,idx):
    global len_bsort,max_idx
    
    mid = (left+right)//2
    if bsort[mid][1] < value:
        if mid+1 == right:
            if right == len_bsort:
                bsort.append([len_bsort,value])
                length.append(len_bsort)
                len_bsort+=1
                max_idx = idx
                return
            else:
                bsort[right][1] = value
                length.append(bsort[right][0])
                return
        bsearch(mid+1,right,value,idx)
        
    elif bsort[mid][1] > value:
        if left == mid:
            bsort[left][1] = value
            length.append(bsort[left][0])
            return
        bsearch(left,mid,value,idx)
    else:
        length.append(bsort[mid][0])
        return 
    

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

bsort = [[0,0]]
len_bsort = 1
length = []
max_idx = -1
for i in range(len(arr)):
    idx = i
    value = arr[i]
    bsearch(0,len_bsort,value,idx)

print(len_bsort -1)
result = [arr[max_idx]]
max_value = length[max_idx]-1
for i in reversed(range(max_idx)):
    if max_value == length[i]:
        result.append(arr[i])
        max_value -= 1
for i in reversed(result):
    print(i,'',end='')