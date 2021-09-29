import sys

def same(left_idx,right_idx): #left~right중 최대값 기준으로 왼쪽count, 오른쪽 count 해서 더해주는 함수
    
    if left_idx == right_idx: #양쪽끝에서 생기는 문제인데 이거는 0을 반환하도록 밑에서 return값의 type이 int인것 기준으로 생각하는부분
        return 0
    elif right_idx - left_idx == 1: #차이가 한개짜리면 그저 count는 0개지만 max값이 arr[left_idx]가 되도록
        return (0,arr[left_idx])
    Max = 0
    Max_idx = 0

    for i in range(left_idx,right_idx):
        if Max<arr[i]:
            Max = arr[i]
            Max_idx = i
    #최대값 찾았으니
    right = same(Max_idx+1,right_idx)
    #오른쪽 카운트와 최대값
    left = same(left_idx, Max_idx)
    #왼쪽 카운트와 최대값
    
    if type(left) == int:
        right_count, right_max =right
        return(Max - right_max + right_count, Max)

    elif type(right) == int:
        left_count, left_max =left
        return(Max - left_max + left_count, Max)
    #둘중에 하나가 끝부분이면 한쪽부분만 count
    else:
        #아니면 이제 완전히 다 있다는거니까 현재 Max값 기준으로 왼쪽은 얼마나 더올려야되고 오른쪽은 얼마나 더올려야되는지 합해서 return
        left_count,left_max = left
        right_count, right_max = right
        return (Max - left_max+left_count + Max - right_max + right_count, Max)

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

print(same(0,n)[0])