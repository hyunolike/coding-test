N = list(input().strip())
ans = []
Op = []
rank = {'(':0, '+':1, '-':1, '*':2, '/':2}

for i in N:
    if i == '(':
        Op.append(i)
    elif i == ')':     
        while Op[-1] != '(':
            ans.append(Op.pop())
        Op.pop()     
    elif i =='+' or i =='*' or i =='/' or i =='-' :
        if len(Op) == 0:
            Op.append(i)
        else:
            if rank[i] == rank[Op[-1]]:  
                ans.append(Op.pop())
                Op.append(i)
            elif rank[i] > rank[Op[-1]]: 
                Op.append(i)
            elif rank[i] < rank[Op[-1]]:
                while len(Op) > 0 and rank[i] <= rank[Op[-1]]:
                    ans.append(Op.pop())
                Op.append(i)
    else:
        ans.append(i)


for p in range(len(Op)):
    ans.append(Op.pop())

for j in range(len(ans)):
    print(ans[j],end="")

    
