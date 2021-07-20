import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
sentences = [deque(input().rstrip().split()) for _ in range(n)]
L = deque(input().rstrip().split())


while L:
    top = L.popleft()

    for i in range(len(sentences)):
        if sentences[i] and top == sentences[i][0]:
            sentences[i].popleft()
            ans = "Possible"
            break
        else:
            ans = "Impossible"
    if ans == "Impossible":
        break

# L이 끝났는데, 앵무새가(sentences)가 말을 다 못하면 실패임
for i in range(len(sentences)):
    if sentences[i]:
        ans = "Impossible"
        break

print(ans)
