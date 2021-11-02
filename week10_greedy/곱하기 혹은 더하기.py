# 307
num=list(map(int, input()))
first=num[0]
answer=0
for i in range(1, len(num)):
    second=num[i]
    if first*second<=1: # 0이거나, 1일 경우 더하기
        result=first+second
        answer=result
    else: # 0이나 1이 아닐 경우 곱하기
        result=first*second
        answer=result
    first=result
print(result)

# another solution
data = input()
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num=int(data[i])
    if num<=1 or result<=1:
        result += num
    else:
        result *= num
print(result)