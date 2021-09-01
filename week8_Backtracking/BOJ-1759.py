#1759 암호만들기

"""
문제풀이 1:

"""
l,c = map(int,input().split())
str_s = list(map(str,input().split()))
str_s.sort()

con1 = ['a','e','i','o','u']
visited = [0]*c

def recursive_str(cnt,str_):
    global con1,visited,str_s
    #print(cnt,str_)
    if(cnt==l):
        #순환끝
        #조건 부합한지 확인
        count_con1 = 0
        for i in con1:
            count_con1 += str_.count(i)

        #print(count_con1)
        con2=1
        if(count_con1>=1 and len(str_)-count_con1>=2):
            for i in range(len(str_)-1):
                if(str_s.index(str_[i])>str_s.index(str_[i+1])):
                    con2 = 0
            if(con2):
                print(str_)
    else:
        if(len(str_)>1):
            for i in range(len(str_s)):
                if(visited[i]==0):
                    if(str_s.index(str_[-1])<i):
                        visited[i]=1
                        str_ += str_s[i]
                        recursive_str(cnt + 1, str_)
                        visited[i] = 0
                        str_ = str_[:-1]

        else:
            for i in range(len(str_s)):
                if(visited[i]==0):
                    visited[i]=1
                    str_ += str_s[i]
                    recursive_str(cnt+1,str_)
                    visited[i]=0
                    str_ = str_[:-1]


recursive_str(0,'')