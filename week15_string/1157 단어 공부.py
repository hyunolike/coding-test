# https://www.byfuls.com/programming/read?id=49
inputData = input().upper()
searchKeys = list(set(inputData))
 
countArr = []
for key in searchKeys:
    countArr.append(inputData.count(key))
 
if countArr.count(max(countArr)) > 1:
    print("?")
else:
    print(searchKeys[countArr.index(max(countArr))])

""" another Version
from collections import defaultdict
word=input().upper()
cnt_dict=defaultdict(int)

for w in word:
    cnt_dict[w]+=1

answer,value=0,0
for k,v in cnt_dict.items():
    if value<v:
        value=v
        answer=k

cnt_list=list(cnt_dict.values())
if cnt_list.count(max(cnt_list))>=2:
    answer='?'
print(answer)
"""