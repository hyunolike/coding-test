import sys


def dfs(idx,result):
    if idx == n+1:
        for i in range(1,n+1):
            print(result[i],end='')
        sys.exit()
    compare = idx//2
    for this_turn in possible:
        flag = 1
        for i in range(compare):
            count = i + 1
            compare_idx = idx - count
            compare_string = str()
            string = this_turn
            for k in range(count):
                compare_string = compare_string + result[compare_idx - k]
            for k in range(1,count):
                string = string + result[idx - k]
            if string == compare_string:
                flag = 0
                break
        if flag:
            dfs(idx+1, result+this_turn)
        
        
n = int(sys.stdin.readline())

result ='0'

possible = ['1','2','3']

dfs(1,result)