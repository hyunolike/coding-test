from collections import defaultdict
def solution(clothes):
    answer = 1
    hashmap = defaultdict(list)
    
    for name, type in clothes:
        hashmap[type].append(name)
    
    for k, v in hashmap.items():
        answer *= len(v)+1
    
    return answer-1