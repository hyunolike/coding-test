n=int(input())
for _ in range(n):
    case=list(map(str, input()))
    score,total=0,0
    for c in case:
        if c=='O':
            score+=1
            total+=score
        else:
            score=0
    print(total)
