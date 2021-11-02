#309 : 해당 문제는 풀이를 참고했음 -> 그리디 연습 필요한 상태
n=int(input())
coin=list(map(int, input().split()))
coin.sort()

target=1
for x in coin:
    if target < x:
        break
    target += x

print(target)