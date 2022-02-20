n = int(input()) 
word = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(n)] 
alpha = [0] * 26 
print(word)
for i in range(n): 
    j = 0 
    for w in word[i][::-1]: 
        alpha[w] += (10 ** j) 
        j += 1 
print(alpha)
alpha.sort(reverse=True) 
print(alpha)
ans, t = 0, 9 
for i in range(26): 
    if alpha[i] == 0: 
        break 
    ans += (t * alpha[i]) 
    t -= 1 
print(ans)
