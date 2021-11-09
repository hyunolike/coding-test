# 윤년: 4로 나누어 떨어지면 윤년이다. 100으로 나누어떨어지지 않는다.
# 윤년: 400으로 나누어 떨어지면 윤년이다.
def solution(a, b):
    # 0123456: 금토일월화수목
    total=0
    hash={0:'FRI',1:'SAT',2:'SUN',3:'MON',4:'TUE',5:'WED',6:'THU'}
    for i in range(1, a):
        if i in [1,3,5,7,8,10,12]:
            total+=31
        elif i in [4,6,9,11]:
            total+=30
        else:
            total+=29
    total+=b-1
    total=total%7
    
    return hash[total]

# another solution
def getDayName(a,b):
    months=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=['FRI','SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

