def solution(n, arr1, arr2):
    answer=[[0]*n for _ in range(n)]
    map1,map2=[],[]
    
    for a in arr1:
        tmp=''
        while a!=0:
            tmp+=str(a%2)
            a=a//2
        while len(tmp)<n:
            tmp+='0'
        tmp=list(map(int, tmp))
        tmp.reverse()
        map1.append(tmp)
    for a in arr2:
        tmp=''
        while a!=0:
            tmp+=str(a%2)
            a=a//2
        while len(tmp)<n:
            tmp+='0'
        tmp=list(map(int, tmp))
        tmp.reverse()
        map2.append(tmp)
    
    for i in range(len(map1)):
        for j in range(len(map1)):
            if map1[i][j]+map2[i][j]:
                answer[i][j]='#'
            elif map1[i][j]==map2[i][j]==0:
                answer[i][j]=' '
    answer=[''.join(a) for a in answer]
    
    return answer

# another solution
import re

def solution(n, arr1, arr2):
    answer=['#']*n
    for i in range(0, n):
        answer[i]=str(bin(arr1[i]|arr2[i]))[2:]
        answer[i]=re.sub('1','#','0'*(n-len(answer[i]))+answer[i])
        answer[i]=re.sub('0',' ', answer[i])
    return answer
