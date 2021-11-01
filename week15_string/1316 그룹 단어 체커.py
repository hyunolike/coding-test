n=int(input())
answer=0
for _ in range(n):
    word=input()
    space=set()
    flag=True
    for i in range(1, len(word)):
        if word[i]!=word[i-1]:
            if word[i] in space:
                flag=False
                break
            else:
                space.add(word[i-1])
    if flag:
        answer+=1
print(answer)