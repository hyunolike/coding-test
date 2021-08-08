#1300 K번째수  

#문제풀이 : 1.N의 범위가 매우크기 때문에 이진 탐색 사용생각
#2. 우리가 구해야되는것은 B[k] 즉 B베열의 k순서의 숫자이다.
#3. 이때 배열 B는 규칙성을 가지고 있으므로 그 규칙을 이용해서 분할을 구현
#규칙 = B는 구구단과 같다 따라서 각 n단의 우리가 특정하는숫자보다 작은것이 몇개있는지
#추측 가능하다. ex)  10x10 일때 5단에  38보다 작은수는 38/5 = 7개있다.
# 이러한 규칙으로 우리가원하는 k번째수보다 k-1개숫자가앞에있으면 그순간 답이된다

import sys
input =sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())


start = 1
end = N*N
#B[k]는 1~ N*N까지 가능

while start <= end:
    mid = (start + end ) //2
    count = 0
    #각 단의 mid값 보단 작은수의 갯수를 카운트
    for i in range(1,N+1):
        
        count += min(mid//i,N)
        print(mid//i , count)
        
    # 만약에 카운트가 k보다 크다면 mid가 k보다 크기 때문에 줄여준다
    if count >= K :
        end = mid -1
    else:
        start = mid+1
    # start > end가될때의 mid가 답일수밖에 없으므로 start 를 출력
print(start)