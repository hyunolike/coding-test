#7490 0 만들기

"""
문제풀이 1:
"""

import sys
input = sys.stdin.readline

tc = int(input())

def solv():
    global n,answer
    n = int(input())
    answer = []
    select_operator(2,'1')
    print()
def select_operator(now,ans):
    global answer
    if now == n+1:
        calc(ans)
        return

    select_operator(now+1,ans+' '+str(now))
    select_operator(now+1,ans+'+'+str(now))
    select_operator(now+1,ans+'-'+str(now))

def calc(ans):
    tmp = ans.replace(' ','')
    if eval(tmp) == 0:
        print(ans)
for _ in range(tc):
    solv()