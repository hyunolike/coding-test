from itertools import combinations, permutations
target=int(input())

list=[]
for i in range(10):
    list.append(i)

combo=permutations(list,7)

#67002
#42801
#109803

result=-1
for i in combo:
    if i[0]!=0 and i[4]!=0:
        hello=i[0]*10000 + i[1]*1000 + i[2] * 110 + i[3]
        world=i[4]*10000 + i[3]*1000 + i[5]*100 + i[2]*10 + i[6]
        if (hello+world) == target:
            result = hello+world
            break
if result==-1:
    print('No Answer')
else:
    print(' ',hello)
    print('+',world)
    print('-------')
    if target>=100000:
        print('',target)
    else:
        print(' ',target)
