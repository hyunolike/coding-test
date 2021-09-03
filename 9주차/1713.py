N=int(input())
recommends=int(input())
student=list(map(int,input().split()))
count=0
result=[]


for i in range(len(student)):

    if len(result)==N:
        result.sort(key=lambda x:(x[1],x[2]))
        print(result)
        ff=True
        for j in range(N):
            if student[i]==result[j][0]:
                ff=False
                result[j]=[result[j][0],result[j][1]+1,result[j][2]]
        if ff==True:
            result[0]=[student[i],1,count]
        
    else:
        flag=True
        for j in range(N):
            try:
                if student[i]==result[j][0]:
                    result[j]=[result[j][0],result[j][1]+1,result[j][2]]
                    flag=False
                    break
            except:
                pass
        if flag == True:
            result.append([student[i],1,count])

    count+=1
print(result)
result.sort()
for i in range(N):
    try:
        print(result[i][0],end=' ')
    except:
        pass
print()










