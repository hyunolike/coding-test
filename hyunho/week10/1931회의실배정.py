n = int(input())
meet_info = [[0]*2 for _ in range(n)]
for i in range(n):
  s, e = map(int, input().split())
  meet_info[i][0] = s
  meet_info[i][1] = e

meet_info.sort(key=lambda x : (x[1], x[0]))

cnt = 1
end_time = meet_info[0][1]

for i in range(n): 
  if meet_info[i][0] >= end_time:
    cnt += 1
    end_time = meet_info[i][1]
  
print(cnt)
    