import sys



n, k = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

length = 0
Max_length = 0
number_dict = dict()
i = 0
while i<n:

    if arr[i] in number_dict:
        if number_dict[arr[i]][0]+1> k:
            Max_length = max(length,Max_length)
            i = number_dict[arr[i]][1]+1
            number_dict = dict()
            length=0
            
        else:
            number_dict[arr[i]][0]+=1
            length+=1
            i+=1
    else:
        number_dict[arr[i]] = [1,i]
        length+=1
        i+=1
Max_length = max(Max_length,length)

print(Max_length)