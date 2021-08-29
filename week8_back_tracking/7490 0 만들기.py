
def DFS(L, ans):
    if L==n-1:
        answer = ''.join(map(str, ans))
        answer = eval(answer)
        if answer == 0:
            for a in ans:
                if a == '':
                    print(' ', end='')
                elif a == n:
                    print(a)
                else:
                    print(a, end='')
    else:
        ans.insert(L*2+1, '')
        DFS(L+1, ans)
        ans.pop(L*2+1)

        ans.insert(L*2+1, '+')
        DFS(L+1, ans)
        ans.pop(L*2+1)

        ans.insert(L*2+1, '-')
        DFS(L+1, ans)
        ans.pop(L*2+1)

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [i for i in range(1, n+1)] # 1부터 7까지 저장
    DFS(0, nums)
    print('')