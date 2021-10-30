n=int(input())
answer=0
for _ in range(n):
    word=input()
    ch=[word[0]]
    group=True
    for i in range(1, len(word)):
        if word[i]!=word[i-1]:
            if word[i] in ch:
                group=False
                break
            else:
                ch.append(word[i])
    if group:
        answer+=1
print(answer)