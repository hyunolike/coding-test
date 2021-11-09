def solution(nums):
    ''' https://programmers.co.kr/learn/courses/30/lessons/1845

    Notes:
        1. 2/N 마리 수를 계산한다.
        2. 폰켓몬 리스트를 set으로 만든 뒤 길이를 계산한다.
        3. 마리수가 폰켓몬 길이보다 작으면 해당값을 마리수를 리턴한다.
        4. 마리수가 폰켓몬 길이보다 크면 폰켓몬 길이를 리턴한다.

    Args:
        nums (list): 폰켓몬 종류 번호(int)를 담은 리스트

    Returns:
        answer (int): 선택할 수 있는 폰켓몬 종류 최대 개수
 
    '''

    cnt = len(nums)//2
    nums = set(nums)
    
    if cnt < len(nums):
        return cnt
    else:
        return len(nums)

# another solution
def solution(nums):
    kind=set(nums)
    cnt=len(nums)//2
    if len(kind)>cnt:
        return cnt
    else:
        return len(kind)