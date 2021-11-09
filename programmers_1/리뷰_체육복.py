def solution(n, lost, reserve):
    new_lost=set(lost)-set(reserve)
    new_reserve=set(reserve)-set(lost)
    for l in new_lost:
        if l-1 in new_reserve:
            new_reserve.remove(l-1)
        elif l+1 in new_reserve:
            new_reserve.remove(l+1)
        else:
            n-=1
    return n