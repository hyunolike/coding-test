# 시간초과 or 메모리 초과
# def visit(length, x, y):
#     global answer
#     if length > 2:
#         visit(length//2, x, y)
#         visit(length//2, x, y+length//2)
#         visit(length//2, x+length//2, y)
#         visit(length//2, x+length//2, y+length//2)
#     else:
#         res[(x,y)] = answer; answer+=1
#         res[(x,y+1)] = answer; answer+=1
#         res[(x+1,y)] = answer; answer+=1
#         res[(x+1,y+1)] = answer; answer+=1

n, r, c = map(int, input().split())
answer = 0

while n > 1:
    size = (2**n) // 2
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        answer += size ** 2
        c -= size
    elif r >= size and c < size:
        answer += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:
        answer += size ** 2 * 3
        r -= size
        c -= size
    n -= 1

if r==0 and c==0:
    print(answer)
elif r==0 and c==1:
    print(answer+1)
elif r==1 and c==0:
    print(answer+2)
elif r==1 and c==1:
    print(answer+3)
