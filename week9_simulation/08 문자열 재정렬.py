#316

s=input()
alpha=[a for a in s if a.isalpha()]
digit=[int(d) for d in s if d.isdigit()]
alpha.sort()
total=sum(digit)
print(''.join(alpha)+str(total))

# another solution
data=input()
result=[]
value=0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value+=int(x)

# 알파벳을 오름차순으로 정렬
result.sort()
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))