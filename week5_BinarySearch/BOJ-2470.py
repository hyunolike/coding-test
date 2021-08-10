# 2470 두 용액

# 투포인터 /슬라이딩 윈도우

#문제풀이:


import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
arr = sorted(arr)

start = 0
end = N-1
ans_s = 0
ans_e = N-1
mid =abs(arr[start]+arr[end])


while start<end:
    if abs(arr[start]+arr[end])<mid:
        mid=abs(arr[start]+arr[end])
        ans_s = start
        ans_e = end
        
    start_a = arr[start+1]+arr[end]
    end_a = arr[start]+arr[end-1]
    
    if abs(start_a)<abs(end_a):
        start+=1
    else:
        end-=1
        
print(arr[ans_s],arr[ans_e])