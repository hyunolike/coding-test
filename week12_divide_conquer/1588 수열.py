def get_count(x, sec, start, end):
    length = 3**sec # x 변환한 길이 계산 
    # 종료 조건: 범위 안에 수가 없으면 0리턴
    if length <= start or end < 0:
        return [0, 0, 0]
    
    # 구간이 전체 범위를 포함하는 경우
    # <= : 아직 변환이 완료된 것이 아닐 수 있음
    if start <= 0 and length-1 <= end:
        answer = [0, 0, 0]
        answer[x-1] += 1 # 시작값 + 1
        for i in range(sec): # sec초만큼 변환
            temp = answer[:]
            answer[0] = temp[0]+temp[1]*2
            answer[1] = temp[0]+temp[1]+temp[2]*2
            answer[2] = temp[0]+temp[2]
        return answer # length 전부를 계산해서 반환

    # 구간을 전부 계산할 필요가 없는 경우 [특정 구간으로 주어짐]
    changed = ((1, 3, 2), (2, 1, 1), (2, 3, 2)) # 1,2,3 변환
    answer = [0, 0, 0]
    for i in range(3): # sec-1 : 1번 변환 수행
        part = get_count(changed[x-1][i], sec-1, start-length/3*i, end-length/3*i)
        for j in range(3):
            answer[j] += part[j]
    
    return answer

x=int(input())
start=int(input())
end=int(input())
n=int(input())
print(' '.join(map(str, get_count(x, n, start, end))))