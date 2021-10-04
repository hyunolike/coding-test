n, k = map(int, input().split())
s = list(map(int, input().split()))
answer = 0
length = 0
l, r = 0, 0
cnt = k

while True:
    if r >= len(s): # 종료조건
        break
    if s[r]%2 == 0: # 짝수라면 길이 증가
        r += 1
        length += 1
    else: # 아닐 경우 k가 가능한 지 체크
        if cnt: # k가 존재함
            cnt -= 1
            r += 1
        else: # k 불가능
            if s[l]%2 == 0: # l번째가 짝수일 때
                l += 1
                length -= 1 # 길이 감소
            else: # l번째가 홀수일 때
                l += 1
                cnt += 1
    answer = max(answer, length)
print(answer)