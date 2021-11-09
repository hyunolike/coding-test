def solution(numbers):
    answer = []
    check=[0]*(sum(numbers)+1)
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            total=numbers[i]+numbers[j]
            if check[total]==0:
                check[total]=1
    answer=[idx for idx, c in enumerate(check) if c==1]
    
    return answer

# another solution
def solution(numbers):
    answer=[]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))