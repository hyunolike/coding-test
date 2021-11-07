#315

score=input()
front=score[:len(score)//2]
back=score[len(score)//2:]
if sum(map(int, front)) == sum(map(int, back)):
    print("LUCKY")
else:
    print("READY")

# another solution
n=input()
length=len(n)
summary=0

# 왼쪽 부분 자릿수 합 더하기
for i in range(length//2):
    summary+=int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length//2, length):
    summary-=int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한 지 검사
if summary==0:
    print("LUCKY")
else:
    print("READY")
