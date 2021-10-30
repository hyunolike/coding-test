# https://ooyoung.tistory.com/74

word=input()
answer=0
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia:
    word = word.replace(i, '*')
print(len(word))