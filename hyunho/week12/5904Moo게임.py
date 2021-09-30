g=lambda i:(i<<2)-bin(i).count('1') 
i=int(input())-1 
n=max((i//4)-9,0) 
while g(n)<i:n+=1 
print('om'[g(n)==i])

