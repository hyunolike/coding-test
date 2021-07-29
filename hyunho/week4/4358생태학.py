import sys
from collections import defaultdict

input = lambda : sys.stdin.readline()

trees = defaultdict(int)
count = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    count += 1

tree_lst = list(trees.keys())
tree_lst.sort()
for tree in tree_lst:
    print(f'{tree} {trees[tree]/count*100:.4f}')