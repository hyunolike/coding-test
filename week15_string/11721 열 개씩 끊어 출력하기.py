word=input()
while word:
    if len(word)<=10:
        break
    tmp=word[:10]
    word=word[10:]
    print(tmp)
print(word)