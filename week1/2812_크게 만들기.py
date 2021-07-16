def first(data, k):
    '''
        Notes:
            1. Stack이 차있고 top보다 n이 크며, cnt가 k가 아닐 경우 Stack의 top을 pop
            2. 1번에 해당하지 않으면 Stack에 n을 push
            3. k개만큼 pop하지 않았다면 Stack에서 남은 개수만큼 pop
    '''
    stack = []
    cnt = 0
    for n in data:
        while stack and stack[-1]<n and cnt !=k:
            stack.pop()
            cnt+=1
        stack.append(n)
    while cnt != k:
        stack.pop()
        cnt += 1
    for a in stack:
        print(a, end='')

n, k = map(int, input().split())
data = input()
first(data, k)