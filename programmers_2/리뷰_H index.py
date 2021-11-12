from bisect import bisect_left

def solution(citations):
    citations.sort()
    for idx in range(len(citations),-1,-1):
        small=bisect_left(citations, idx)
        up=len(citations)-small
        
        if up>=idx: return idx

# another solution
def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# another solution
def solution(citations):
    citations=sorted(citations)
    length=len(citations)
    for i in range(length):
        if citations[i]>=length-i:
            return length-i
    return 0