import sys

lst = [list(sys.stdin.readline().strip()) for _ in range(2)]
alpha_s = dict()
alpha_s['A'] = lst[0].count('A')
alpha_s['B'] = lst[0].count('B')

alpha_t = dict()
alpha_t['A'] = lst[1].count('A')
alpha_t['B'] = lst[1].count('B')




for i in reversed(range(len(lst[0]), len(lst[1]))):
    if alpha_s[lst[1][i]] == alpha_t[lst[1][i]]:
        print(0)
        sys.exit()
    if lst[1][i] == 'A':
        alpha_t['A'] -= 1
    else:
        alpha_t['B'] -= 1
        for j in range(i//2):
            lst[1][j] ,lst[1][i-1-j]= lst[1][i-1-j],lst[1][j]
  
for i in range(len(lst[0])):
    if lst[0][i] != lst[1][i]:
        print(0)
        sys.exit()

print(1)