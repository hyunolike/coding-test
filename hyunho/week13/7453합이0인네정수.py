import sys

number = int(sys.stdin.readline())
a_list, b_list, c_list, d_list = [], [], [], []
for _ in range(number):
    a, b, c, d = map(int,sys.stdin.readline().split())
    a_list.append(a); b_list.append(b); c_list.append(c); d_list.append(d)

a_b_dict = dict()
for a in a_list:
    for b in b_list:
        a_b_dict[a+b] = a_b_dict.get(a+b, 0) + 1

count = 0
for c in c_list:
    for d in d_list:
        count += a_b_dict.get(-(c+d),0)

print(count)
