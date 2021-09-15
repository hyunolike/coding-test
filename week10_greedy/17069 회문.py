# val == val[::-1]로 바로 체크 시 시간초과 발생
# 유사 회문 검사 시 시간초과, 고로 투 포인터로 구현
# 시간복잡도가 낮은 이유는, 다 비교하지 않더라도 중간에 return할 수 있기 때문

def check_pseudo(val, l, r):
    while l<r:
        # 회문 체크
        if val[l]==val[r]:
            l+=1
            r-=1
        else:
            return False
    return True

def check_answer(val, l, r):
    if val == val[::-1]:
        # 일단 회문체크
        return 0
    else:
        # 유사회문체크
        while l<r:
            if val[l]==val[r]:
                l+=1
                r-=1
            else:
                case1=check_pseudo(val, l+1, r)
                case2=check_pseudo(val, l, r-1)
                if case1 or case2:
                    return 1
                else:
                    return 2

cases = int(input())
for _ in range(cases):
    val = input()
    l, r = 0, len(val)-1
    print(check_answer(val, l, r))