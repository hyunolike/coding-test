def get_count(x, sec, left, right):
    length = 3**sec # x 변환한 길이 계산 
    # 종료 조건: 범위 안에 수가 없으면 X
    if length <= left or right < 0:
        return [0, 0, 0]
    
    # 시작이 0이거나 구간끝이 변환한 길이보다 큼
    if left <= 0 and length-1 <= right: 
        answer = [0, 0, 0]
        answer[x-1] += 1 # 시작값 + 1
        for i in range(sec): # sec초만큼 변환
            temp = answer[:]
            answer[0] = temp[0]+temp[1]*2
            answer[1] = temp[0]+temp[1]+temp[2]*2
            answer[2] = temp[0]+temp[2]
        return answer

    # length별 값을 계산 후 answer를 구해야 하는 경우
    changed = ((1, 3, 2), (2, 1, 1), (2, 3, 2))
    answer = [0, 0, 0]
    for i in range(3):
        part = get_count(changed[x-1][i], sec-1, left-length/3*i, right-length/3*i)
        for j in range(3):
            answer[j] += part[j]
    
    return answer

x=int(input())
left=int(input())
right=int(input())
n=int(input())
print(' '.join(map(str, get_count(x, n, left, right))))