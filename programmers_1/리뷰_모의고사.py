def solution(answers):
    answer = []
    # 12345 : 4
    # 21 23 24 25 : 7
    # 33 11 22 44 55 : 9
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    cnt=[0,0,0]

    for i in range(len(answers)):
        if answers[i]==one[i%len(one)]: cnt[0]+=1
        if answers[i]==two[i%len(two)]: cnt[1]+=1
        if answers[i]==three[i%len(three)]: cnt[2]+=1
    
    for idx, c in enumerate(cnt, 1):
        if max(cnt)==c:
            answer.append(idx)
    
    return answer