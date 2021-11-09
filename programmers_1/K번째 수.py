def solution(array, commands):
    answer = []
    
    for command in commands:
        s, e, t = command
        cut = array[s-1:e]
        cut.sort()
        answer.append(cut[t-1])
    
    return answer

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        tmp=array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer
