import sys

n = int(sys.stdin.readline())

arr= [list(map(str,sys.stdin.readline().strip()) )for _ in range(n)]

possible_number = list(reversed(range(10)))

length = [len(arr[i]) for i in range(n)]

number_set = []
priority = []
count = 10**7
for i in range(8):
    number_set.append([])
    priority.append(count)
    count //= 10
for i in range(len(length)):
    for j in range(8-length[i],8):
        number_set[j].append(arr[i][j-(8-length[i])])

dictionary = dict()

for i in range(len(number_set)):
    if number_set[i]:
        for j in number_set[i]:
            try:
                dictionary[j] += priority[i]
            except:
                dictionary[j] = priority[i]

dictionary = sorted(dictionary.items(), key = lambda item: item[1], reverse= True)
alpha_set= dict()

for i in range(len(dictionary)):   
    alpha_set [dictionary[i][0]] =  possible_number[i]

num = 0
for i in arr:
    idx = 7
    for j in reversed(i):
        num+=alpha_set[j]*priority[idx]
        idx-=1
print(num)