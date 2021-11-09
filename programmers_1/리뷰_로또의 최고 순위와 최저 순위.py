def solution(lottos, win_nums):
    answer = []
    
    length, zero, cnt = len(lottos), 0, 0
    for l in lottos:
        if l == 0:
            zero += 1
    
    for num in lottos:
        for win in win_nums:
            if num == win:
                cnt += 1
    
    best = cnt + zero
    worst = cnt

    if best < 2: 
        best = 6
    else:
        best = 1 + length - best
    if worst < 2: 
        worst = 6
    else:
        worst = 1 + length - worst        
    
    answer.append(best)
    answer.append(worst)
    return answer

def solution(lottos, win_nums):
    answer=[]
    rank=[6,6,5,4,3,2,1]
    matched=0
    zero = lottos.count(0)
    for num in lottos:
        if num in win_nums:
            matched += 1
    answer.append(rank[matched+zero])
    answer.append(rank[matched])
    
    return answer

def solution(lottos, win_nums):
    answer=[]
    best, worst = 0,0
    
    for t in lottos:
        if t in win_nums:
            worst+=1
    best=worst+lottos.count(0)
    tmp=[best,worst]
    answer=[6 if t<2 else 6-t+1 for t in tmp]
    return answer
