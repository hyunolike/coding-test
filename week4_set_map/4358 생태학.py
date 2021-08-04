import sys

tree = dict()

while True:
    name = sys.stdin.readline().strip()
    if not name:
        break
    if name not in tree.keys():
        tree[name] = 1
    else:
        tree[name] += 1

total = sum(tree.values())
tree = sorted(tree.items(), key = lambda x: x[0])
for data in tree:
    print('{0} {1:.4f}'.format(data[0], data[1]/total * 100))