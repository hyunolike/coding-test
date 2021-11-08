def solution(numbers):
    # 1,2,3,4,6,7,8,0: 5+9=14
    result=0
    
    for i in range(1, 10):
        if i not in numbers:
            result+=i
    if result:
        return result
    else:
        return -1