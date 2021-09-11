import sys
sys.setrecursionlimit(100000)
def check(left_idx,right_idx,flag):
    if flag >= 2:
        return 2
    if left_idx >= right_idx:
        return flag
    else:
        if i[left_idx] == i[right_idx]:
            flag = check(left_idx+1,right_idx-1,flag)
        else:
            left_flag = check(left_idx,right_idx-1,flag+1)
            right_flag = check(left_idx+1,right_idx,flag+1)
            flag = min(left_flag, right_flag)
           
    return flag

n = int(sys.stdin.readline())

arr = [list(map(str,sys.stdin.readline().strip())) for _ in range(n)]
result=[]
for i in arr:
    flag = 0
    print(check(0,len(i)-1,0))

