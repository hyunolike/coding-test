n = int(input())
card = list(map(int, input().split()))

odd_sum = sum(card[1::2])

last_card = card[-1]

ans = odd_sum
sum = card[0]
temp = 0
for i in range(1, len(card)):
    if i % 2:
        temp = sum + odd_sum - card[-1]
        odd_sum -= card[i]

    else:
        temp = sum + odd_sum
        sum += card[i]

    if temp > ans:
        ans = temp

print(ans)
