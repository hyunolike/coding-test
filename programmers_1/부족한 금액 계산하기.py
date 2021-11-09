def solution(price, money, count):
    total=0
    for i in range(1, count+1):
        total+=price*i
    if total-money<=0:
        return 0
    else:
        return total-money

