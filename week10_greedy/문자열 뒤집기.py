#308
data=list(map(int, input()))
zero_cnt, one_cnt=0,0

# 1로 만들기
for i in range(len(data)-1):
    if data[i]==1:
        pass
    elif data[i]==0:
        if i+1 == len(data)-1:
            one_cnt+=1
        elif data[i+1]==0:
            pass
        elif data[i+1]==1:
            one_cnt+=1

# 0으로 만들기
for i in range(len(data)-1):
    if data[i]==0:
        pass
    elif data[i]==1:
        if i+1 == len(data)-1:
            zero_cnt+=1
        elif data[i+1]==1:
            pass
        elif data[i+1]==0:
            zero_cnt+=1
answer=min(one_cnt, zero_cnt)
print(answer)

# another solution
data=input()
count0=0
count1=0

# 첫 번째 원소 처리
if data[0]=='1':
    count0+=1
else:
    count1+=1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1]=='1': # 다음 수에서 1로 바뀌는 경우
            count0+=1
        else: # 다음 수에서 0으로 바뀌는 경우
            count1+=1
print(min(count0, count1))