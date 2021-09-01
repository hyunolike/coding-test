#13140 hello world

"""
문제풀이 1:  혼자힘으로는 못풀어서 다시풀어보기..
"""
import sys
input = sys.stdin.readline
#백트래킹
def backt(depth,ans):
  global count
  if depth == 7:
    hello = s[2]*10000+s[1]*1000+s[3]*110+s[4]
    world = s[6]*10000+s[4]*1000+s[5]*100+s[3]*10+s[0]
    add = hello + world
    if add == ans and s[2] != 0 and s[6] != 0:
      count = 1
      print(" ",hello)
      print('+',world)
      print('-------')
      if ans < 100000:
        print(" ",ans)
      else:
        print(" ",end='')
        print(ans)
      sys.exit()
    return
  
  for i in range(10):
    if i not in s:
      s.append(i)
      backt(depth+1,ans)
      s.pop()

#입력
ans = int(input())
s = []#dehlorw
count = 0
backt(0,ans)#10개중 7개

#결과(없을 경우)
if count == 0:
  print('No Answer')