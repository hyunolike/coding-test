from collections import defaultdict

def solution(genres, plays):
    answer = []
    gdict = defaultdict(int)
    pdict = defaultdict(list)
    
    for genre,play in zip(genres, plays):
        gdict[genre]+=play
    gdict = sorted(gdict.items(), key=lambda x: x[1], reverse=True)
    gdict = [genre for genre, plays in gdict]
    
    for i in range(len(genres)):
        pdict[genres[i]].append([i, plays[i]])
    
    for i in range(len(genres)):
        pdict[genres[i]] = sorted(pdict[genres[i]], key=lambda x: x[1], reverse=True)
    
    for genre in gdict:
        tmp = pdict[genre][:2]
        for idx, plays in tmp:
            answer.append(idx)
    
    return answer