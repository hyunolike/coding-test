import sys

def dfs(count, index):
    if index == -1:
        if len(set(alpha.values())) == 7 and alpha['h'] != 0 and alpha['w'] != 0:
            print('  %d%d%d%d%d'%(alpha['h'],alpha['e'],alpha['l'],alpha['l'],alpha['o']))
            print('+ %d%d%d%d%d'%(alpha['w'],alpha['o'],alpha['r'],alpha['l'],alpha['d']))
            print('-------')
            if len(arr) == 6:
                print(' %d%d%d%d%d%d'%(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5]))
            else:
                print('  %d%d%d%d%d'%(arr[0],arr[1],arr[2],arr[3],arr[4]))
            sys.exit()
    if index == 3:
        aim = arr[-2]
        for i in range(10):
            if (i+i+count) % 10 == aim:
                num = i+i+count
                ten_count = 0
                while num >= 10:
                    num -= 10
                    ten_count+=1
                alpha['l'] = i
                dfs(ten_count, 2)
    elif index == 2:
        aim = arr[-3]
        for i in range(10):
            if (alpha['l'] + i + count) % 10 == aim:
                num = alpha['l']+i+count
                ten_count = 0
                while num >= 10:
                    num -= 10
                    ten_count+=1
                alpha['r'] = i
                dfs(ten_count, 1)
    elif index == 1:
        aim = arr[-4]
        for i in range(10):
            if (alpha['o'] + i + count) % 10 == aim:
                num = alpha['o']+i+count
                ten_count = 0
                while num >= 10:
                    num -= 10
                    ten_count+=1
                alpha['e'] = i
                dfs(ten_count, 0)
    elif index == 0:
        if len(arr) == 6:
            aim = arr[0]*10+arr[1]
            for i in range(10):
                for j in range(10):
                    if i+j+count == aim:
                        alpha['w'] = i
                        alpha['h'] = j
                        dfs(0,-1)
        else:
            aim = arr[0]
            for i in range(10):
                for j in range(10):
                    if i+j+count == aim:
                        alpha['w'] = i
                        alpha['h'] = j
                        dfs(0,-1)


arr = list(map(int,sys.stdin.readline().strip()))

alpha = {'h': 0, 'e':0, 'l' : 0, 'o':0, 'w':0, 'r':0, 'd' :0}

if len(arr) >6:
    print('No Answer')
    sys.exit()


for i in range(10):
    for j in range(10):
        if (i+j) % 10 == arr[-1]:
            num = i+j
            count = 0
            while num >= 10:
                num -= 10
                count +=1
            alpha['o'] = i
            alpha['d'] = j
            dfs(count,3)
            alpha['d'] = j
            alpha['o'] = i
            dfs(count,3)

print('No Answer')