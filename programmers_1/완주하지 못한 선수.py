from collections import defaultdict

def solution(participant, completion):
    answer = ''
    start = defaultdict(int)
    
    for p in participant:
        start[p] += 1
    
    for c in completion:
        start[c] -= 1
    
    for k, v in start.items():
        if v != 0:
            answer = k  
    
    return answer


def solution(participant, completion):
    from collections import defaultdict
    phash=defaultdict(int)
    chash=defaultdict(int)
    
    for c in completion:
        chash[c]+=1
    for p in participant:
        phash[p]+=1
    for p in participant:
        if p not in chash:
            return p
        elif chash[p]!=phash[p]:
            return p
