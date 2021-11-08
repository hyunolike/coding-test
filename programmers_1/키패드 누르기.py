def solution(numbers, hand):
    '''
    Notes:
        1. 왼손, 오른손 현재 위치를 저장하는 자료구조 생성
        2. 1,4,7이면 왼손을 3,6,9면 오른손으로 입력
        3. 2,5,8,0이면 왼손, 오른손과의 거리 계산 후 작은 손 선택
        4. 왼손, 오른손 거리가 같을 경우 hand의 선택에 따라 선택
    
    Args:
        numbers (list): 입력할 키패드 숫자(int)를 담은 리스트
        hand (str): 왼, 오른손 잡이를 나타내는 문자열
    
    Returns:
        answer (str): 사용한 손 순서를 담은 리스트

    '''
    
    answer = ''
    pad = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']
    ]

    l = [3, 0]
    r = [3, 2]

    for n in numbers:
        for i, p in enumerate(pad):
            if n in p:
                target = [i, p.index(n)]
                break
        if n in [1,4,7]:
            l = target
            answer += 'L'
        elif n in [3,6,9]:
            r = target
            answer += 'R'
        elif n in [2,5,8,0]:
            print(f'n={n}, l={l}, r={r}, target={target}')
            lp = [abs(target[0]-l[0]), abs(target[1]-l[1])]
            rp = [abs(target[0]-r[0]), abs(target[1]-r[1])]

            if sum(lp) < sum(rp):
                l = target
                answer += 'L'
            elif sum(lp) > sum(rp):
                r = target
                answer += 'R'
            elif sum(lp) == sum(rp):
                if hand=='left':
                    l = target
                    answer += 'L'
                else:
                    r = target
                    answer += 'R'
    return answer

# 2차원 배열 인덱싱
# 문자열은 find, 리스트 원소는 index로 접근한다. 단, index는 없을 시 오류 리턴
def solution(numbers, hand):
    answer = ''
    graph=[[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    lx,ly=3,0
    rx,ry=3,2
    for num in numbers:
        for i in range(4):
            for j in range(3):
                if graph[i][j]==num:
                    tx,ty=i,j
        if num in [1,4,7,'*']:
            answer+='L'; lx,ly=tx,ty
        elif num in [3,6,9,'#']:
            answer+='R'; rx,ry=tx,ty
        else:
            ldiff=abs(lx-tx)+abs(ly-ty)
            rdiff=abs(rx-tx)+abs(ry-ty)
            if ldiff<rdiff: 
                answer+='L'; lx,ly=tx,ty
            elif ldiff>rdiff: 
                answer+='R'; rx,ry=tx,ty
            else:
                if hand=='left': answer+='L'; lx,ly=tx,ty
                else: answer+='R'; rx,ry=tx,ty
    
    return answer