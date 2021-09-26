n=int(input())
star = ['  *  ', ' * * ', '*****']
n = n//3

cnt = 0
while n > 1:
    n = n//2
    cnt += 1

def print_star(star):
    length = len(star)
    for i in range(length):
        star.append(star[i] + ' ' + star[i])
        star[i] = ' '*length + star[i] + ' '*length
    
    return star

for i in range(cnt):
    star = print_star(star)

for s in star:
    print(s)