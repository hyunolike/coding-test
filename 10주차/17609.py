import sys

input = sys.stdin.readline

T = int(input())

def pali(word):
    i = 0
    n = len(word)
    isPali = True
    part = []
    # 첫번째 pali 검사, 틀린 경우 그부분을 part에 넣어준다. 그것만 검사!
    while i <= (n-1)//2:
        if word[i] != word[n-1-i]:
            isPali = False
            part.append(i)
            part.append(n-1-i)
            break
        i += 1
    if isPali:
        return 0
        
    # part에 있는 알파벳을 차례로 뺀 단어로 다시 검사
    ans = 2
    for j in part:
        i = 0
        likePali = True
        cutword = word[:j] + word[j+1:n]
        while i <= (n-2)//2:
            if cutword[i] != cutword[n-2-i]:
                likePali = False
                break
            i += 1
        if likePali:
            ans = 1
            break
    return ans

for tc in range(1,T+1):
    word = input().strip()
    n = len(word)
    result = pali(word)
    print(result)