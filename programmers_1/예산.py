def solution(d, budget):
    answer = 0
    d.sort()
    for price in d:
        budget-=price
        if budget>=0:
            answer+=1
    return answer

