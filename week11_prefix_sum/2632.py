import sys
import collections

slice = int(sys.stdin.readline())

m, n = map(int,sys.stdin.readline().split())

cut_pizza_a = [int(sys.stdin.readline()) for _ in range(m)]
cut_pizza_b = [int(sys.stdin.readline()) for _ in range(n)]

pizza_a_dict = {0:1}

pizza_b_dict = {0:1}



for i in range(m):
    summation = 0
    for j in range(m):
        
        summation += cut_pizza_a[(i+j)%m]
       
        try:
            pizza_a_dict[summation] += 1
        except:
            pizza_a_dict[summation] = 1



for i in range(n):
    summation = 0
    for j in range(n):
        summation += cut_pizza_b[(i+j)%n]
        try:
            pizza_b_dict[summation] += 1
        except:
            pizza_b_dict[summation] = 1
            
cnt = 0

pizza_a_dict[sum(cut_pizza_a)] = 1
pizza_b_dict[sum(cut_pizza_b)] = 1

for i in range(slice+1):
    try:
        cnt += pizza_a_dict[i]*pizza_b_dict[slice-i]
    except:
        continue
print(cnt)