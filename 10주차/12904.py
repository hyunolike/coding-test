S=input()
T=input()

def minusA(STR):
    return STR[0:-1]

def SubBReverse(STR):
    STR=STR[0:-1]
    return STR[-1::-1]


res=0

while len(T)!=len(S):
    if T[-1]=='A':
        T=minusA(T)
    elif T[-1]=='B':
        T=SubBReverse(T)
if T==S:
    print(1)
else:
    print(0)
    