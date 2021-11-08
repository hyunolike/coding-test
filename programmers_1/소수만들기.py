def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                total=nums[i]+nums[j]+nums[k]
                flag=True
                # total의 최대 약수는 total**0.5이므로
                for l in range(2, int(total**0.5)+1):
                    if total%l==0:
                        flag=False
                        break
                if flag:
                    answer+=1
    return answer

# 에라토스테네스의 체: 소수 판별하기
# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    num=[True]*n

    # n의 최대 약수가 sqrt(n)이하이므로 i=sqrt(n)까지 검사
    m=int(n**0.5)
    for i in range(2, m+1):
        if num[i]==True:
            for j in range(i+i, n, i):
                num[j]=False
    
    # 소수 목록 산출
    return [i for i in range(2, n) if num[i]]
