import sys

def findGroup(idx, target): # 가장 작은 수의 그룹을 찾는 함수
    global n, arr

    lowerBound = 0
    upperBound = n

    for i in range(idx-1, -1, -1):
        if arr[i] != target:
            lowerBound = i+1
            break
    
    for i in range(idx+1, n):
        if arr[i] != target:
            upperBound = i
            break
        
    return (lowerBound, upperBound)

def calculate(lowerBound, upperBound): # 가장 작은 수 그룹의 양옆의 수를 비교하여 그중 작은 수만큼 Add 연산을 수행하는 함수
    global n, arr, minNum, answer

    goalNum = float("inf")

    if lowerBound != 0:
        goalNum = arr[lowerBound-1]
        
    if upperBound != n and arr[upperBound] < goalNum:
        goalNum = arr[upperBound]

    for i in range(lowerBound, upperBound):
        arr[i] = goalNum

    answer += (goalNum - minNum)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    arr = [0] * n

    for i in range(n):
        arr[i] = int(sys.stdin.readline().strip())
        
    maxNum = max(arr)
    minNum = min(arr)

    answer = 0

    while minNum < maxNum: # 현재 회차의 최솟값이 초기 입력이 최댓값이 될 때까지 반복
        minNumIdx = arr.index(minNum)

        lowerBound, upperBound = findGroup(minNumIdx, minNum)

        calculate(lowerBound, upperBound)

        minNum = min(arr)

    print(answer)
