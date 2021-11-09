from bisect import bisect_left, bisect_right

def solution(citations):
    # 0 1 3 5 6
    answer=[]
    citations.sort()
    for i in range(len(citations),-1,-1):
        small=bisect_left(citations, i)
        large=len(citations)-small
        
        if large>=i and small<=i:
            answer.append(i)
    return max(answer)


def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

