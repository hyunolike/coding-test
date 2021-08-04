import operator

n = int(input())

best = dict()
for _ in range(n):
    book = input()
    if book in best.keys():
        best[book] += 1
    else:
        best[book] = 1
    
result = [k for k,v in best.items() if v == max(best.values())]
result.sort()
print(result[0])