import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 앵무새 마리 수
sentences = [deque(input().rstrip().split()) for _ in range(n)]  # 앵무새가 말하는 문장을 담은 큐들의 리스트
L = deque(input().rstrip().split())  # 체크할 문장(큐)


# L로 검사
while L:
    top = L.popleft()  # 맨 앞 단어부터

    for i in range(len(sentences)):  # 앵무새 문장의 집합에서 맨 앞 단어들을 pop
        if sentences[i] and top == sentences[i][0]:  # L.top과 같으면 pop -> possible -> break
            sentences[i].popleft()
            ans = "Possible"
            break
        else:  # 다르면 impossible
            ans = "Impossible"

    if ans == "Impossible":
        break

# L이 끝났는데, 앵무새가(sentences)가 말을 다 못하면 실패
for i in range(len(sentences)):
    if sentences[i]: # 남아있는 단어가 있으면 -> 실패
        ans = "Impossible"
        break

print(ans)

'''
	 1. 앵무새가 말하지 않은 단어를 말했을 때
	 2. 앵무새가 말한 순서대로 말하지 않을 때
	 3. 앵무새가 끝까지 말하지 않았는데 L이 끝났을 때
'''