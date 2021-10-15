word=input()
answer=[]
for i in range(ord('a'), ord('z')+1):
    alpha=chr(i)
    answer.append(word.find(alpha))
print(' '.join(map(str, answer)))