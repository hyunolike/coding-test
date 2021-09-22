n = int(input())
card = list(map(int, input().split()))

mid = n//2
odd, even = card[0::2], card[1::2]

answer = sum(odd)

for i in range(1, mid):
    odd[i] += odd[i-1]
    even[i] += even[i-1]

psum = [[0]+even, [0]+odd]

for i in range(1, n+1):
    idx = i//2+1
    if i%2 == 0:
        res = psum[1][idx-1]+(psum[0][mid-1]-psum[0][idx-2])
    else:
        res = psum[1][idx-1]+(psum[0][mid]-psum[0][idx-1])
    
    answer = max(answer, res)
    
print(answer)