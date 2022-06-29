def solution(dartResult):
    point=[]
    answer=[]
    dartResult=dartResult.replace('10','k')
    point=['10' if i=='k' else i for i in dartResult]
    
    i=-1
    sdt=['S','D','T']
    for j in point:
        if j in sdt:
            answer[i]=answer[i]**(sdt.index(j)+1)
        elif j=='*':
            answer[i]=answer[i]*2
            if i!=0:
                answer[i-1]=answer[i-1]*2
        elif j=='#':
            answer[i]=answer[i]*(-1)
        else:
            answer.append(int(j))
            i+=1
    return sum(answer)

# def solution(dart):
#     answer=0
#     res=[]
#     tmp=''
    
#     for i in range(len(dart)):
#         if dart[i] in ['S','D','T','*','#']:
#             if tmp:
#                 res.append(tmp)
#             res.append(dart[i])
#             tmp=''
#         else:
#             tmp+=dart[i]
    
#     pre,now=0,0
    
#     for i in range(len(res)):
#         if res[i].isdigit():
#             res[i]=int(res[i])
#             if i==0:
#                 pre=i
#             else:
#                 pre=now
#                 now=i
#         elif res[i]=='S':
#             res[now]=res[now]**1
#         elif res[i]=='D':
#             res[now]=res[now]**2
#         elif res[i]=='T':
#             res[now]=res[now]**3
#         elif res[i]=='*':
#             if i<=2:
#                 res[now]=res[now]*2
#             else:
#                 res[now]=res[now]*2
#                 res[pre]=res[pre]*2
#         elif res[i]=='#':
#             res[now]=res[now]*(-1)
    
#     for a in res:
#         try:
#             answer+=a
#         except:
#             continue
#     return answer