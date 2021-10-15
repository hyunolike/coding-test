from collections import defaultdict
word=input()
cnt=defaultdict(int)

for w in word:
    cnt[w.upper()]+=1

answer,value=0,0
for k,v in cnt.items():
    if value<v:
        value=v
        answer=k

cnt=list(cnt.values())
if cnt.count(max(cnt))>=2:
    answer='?'
print(answer)