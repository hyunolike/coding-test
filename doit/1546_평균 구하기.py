n=int(input())
score=list(map(int, input().split()))
sum_n=sum(score)
max_n=max(score)
div_n=n*max_n
print(sum_n/div_n*100)

# Solution 2
# n=input()
# mylist=list(map(int, input().split()))
# mymax=max(mylist)
# sum=sum(mylist)
# print(sum*100 / mymax / int(n)