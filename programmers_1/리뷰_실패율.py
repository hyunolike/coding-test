def solution(N, stages):
    answer = []
    cnt=[0]*(N+2)
    for s in stages:
        for i in range(s+1):
            cnt[i]+=1
    for i in range(1, N+1):
        if cnt[i]==0:
            answer.append((0, i))
        else:
            fail=stages.count(i)/cnt[i]
            answer.append((fail, i))
    answer.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    answer=[i for _, i in answer]
    return answer

# another solution
def solution(N, stages):
    result={}
    denominator=len(stages)
    for stage in range(1, N+1):
        if denominator!=0:
            count=stages.count(stage)
            result[stage]=count/denominator
            denominator-=count
        else:
            result[stage]=0
    return sorted(result, key=lambda x: result[x], reverse=True)
