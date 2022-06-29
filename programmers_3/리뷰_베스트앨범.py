from collections import defaultdict

def solution(genres, plays):
    answer = []
    gdict = defaultdict(int)
    pdict = defaultdict(list)
    
    for genre,play in zip(genres, plays):
        gdict[genre]+=play
    gdict = sorted(gdict.items(), key=lambda x: x[1], reverse=True)
    gdict = [genre for genre, _ in gdict]
    
    for i in range(len(genres)):
        pdict[genres[i]].append([i, plays[i]])
    
    for i in range(len(genres)):
        pdict[genres[i]] = sorted(pdict[genres[i]], key=lambda x: (-x[1], x[0]), reverse=False)
    
    for genre in gdict:
        tmp = pdict[genre][:2]
        for idx, _ in tmp:
            answer.append(idx)
    
    return answer


# another solution
from collections import defaultdict

def solution(genres, plays):
    answer=[]
    kv=defaultdict(int)
    
    for genre, play in zip(genres,plays):
        kv[genre]+=play
    
    kv=list(kv.items())
    kv.sort(key=lambda x: x[1], reverse=True)
    order=[k for k,v in kv]
    
    tmp=defaultdict(list)
    for i in range(len(genres)):
        tmp[genres[i]].append([plays[i],i])
    
    for k in tmp.keys():
        tmp[k].sort(key=lambda x:(x[0],-x[1]), reverse=True)
        tmp[k]=tmp[k][:2]
    
    for o in order:
        t=tmp[o][:2]
        for play, idx in t:
            answer.append(idx)
    
    return answer