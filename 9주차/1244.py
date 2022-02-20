switchNumber=int(input())
switch=list(map(int,input().split()))
studentNumber=int(input())

student = [ list(map(int,input().split())) for _ in range(studentNumber) ]


for ii in range(studentNumber):

    if student[ii][0]==1:
        for jj in range(1,switchNumber+1):
            if 0<(student[ii][1] * jj)<=switchNumber:
                if switch[student[ii][1]*jj-1]==1:
                    switch[student[ii][1]*jj-1]=0
                else:
                    switch[student[ii][1]*jj-1]=1
            else:
                break
        
    elif student[ii][0]==2:
        for kk in range(1,switchNumber+1):
            if (0<student[ii][1]-kk<=switchNumber) and (0<student[ii][1]+kk<=switchNumber):
                if (switch[student[ii][1]-kk-1] == switch[student[ii][1]+kk-1]):
               
                    if switch[student[ii][1]-kk-1]==1:
                        switch[student[ii][1]-kk-1]=0
                        switch[student[ii][1]+kk-1]=0
                    else:
                        switch[student[ii][1]-kk-1]=1
                        switch[student[ii][1]+kk-1]=1
                else:
                    break

        if switch[student[ii][1]-1]==1:
            switch[student[ii][1]-1]=0
        else:
            switch[student[ii][1]-1]=1
        

# 25
# 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
# 1
# 1 1



for i in range(0, switchNumber, 20):
    print(*switch[i:i+20])