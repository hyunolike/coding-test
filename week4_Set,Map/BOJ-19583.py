# 사이버 개강총회(19583) 실버2


#문제풀이 1: 입력받기 2.딕셔너리 사용 
#포인트 : 문자열 입력 및 관리


import sys
input =sys.stdin.readline
log = dict()
ans= 0


start_time, end_time, rend_time = map(str, input().split())
start_time = int("".join(start_time.split(":")))
end_time = int("".join(end_time.split(":")))
rend_time = int("".join(rend_time.split(":")))


while True:
    a = input().rstrip()
    if len(a) < 3:
        break
    time, id = map(str, a.split())
    time = int("".join(time.split(":")))
    if time <=start_time:
        log[id] = 1
    elif end_time <= time <= rend_time:
        if log.get(id) == 1:
            log[id] = 2
            ans += 1

print(ans)