def solution(numbers):
    nums = list(map(str, numbers))
    nums = sorted(nums, key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(nums)))
    
    return answer

# 1. 파이썬 문자열 비교는 1번째를 기준으로 한다. 같으면 2번째 비교.
# 2. int()를 사용하는 이유는 0000인 경우, 0으로 바꾸기 위해서이다.

def solution(numbers):
    numbers=list(map(str, numbers))
    numbers.sort(key=lambda x: x*4, reverse=True)
    return str(int(''.join(numbers)))

