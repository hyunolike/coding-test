import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())

    interviewee=[ list(map(int,input().split())) for _ in range(N) ]
    interviewee.sort()
    print(interviewee)
    temp=interviewee[0][1]
    count=1
    for i in range(1,N):
        if temp > interviewee[i][1]:
            print(interviewee[i],temp)
            count += 1
            temp = interviewee[i][1]
    print(count)
