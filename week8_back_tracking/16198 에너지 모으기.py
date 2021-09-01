def pick(total):
    global answer
    if len(marbles)==2:
        if answer < total:
            answer = total
        return 0
    else:
        for i in range(1, len(marbles)-1):
            value = marbles[i-1]*marbles[i+1]
            tmp = marbles[i]
            del marbles[i]
            pick(total+value)
            marbles.insert(i, tmp)

n = int(input())
marbles = list(map(int, input().split()))
answer = 0
pick(0)
print(answer)