def solution(numbers):
    nums = list(map(str, numbers))
    nums = sorted(nums, key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(nums)))
    
    return answer

# 1. 파이썬 문자열 비교는 1번째를 기준으로 한다. 같으면 2번째 비교.
# 2. int()를 사용하는 이유는 문자열로 바꾸는 과정에서 양 끝 0을 제거한다.