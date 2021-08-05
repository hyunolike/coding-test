# 문제풀이
## 1. [2343 기타 레슨](https://www.acmicpc.net/problem/2343)
![image](https://user-images.githubusercontent.com/44918665/128294339-b305744a-e92d-4e5d-b229-71afe96410c3.png)
### 1.1. 문제유형
- Binary Search
### 1.2. 자료구조
- cnt (int) : 블루레이 개수
- file (int) : 레슨을 저장한 파일 크기
- mid (int) : 블루레이 크기
- left (int) : 가장 작은 블루레이 크기
- right (int) : 가장 큰 블루레이 크기
### 1.3. 해결과정
- 가장 작은 블루레이 크기는 max(lesson), 최대 크기는 sum(lesson)이다.
- 주어진 m개의 블루레이에 강의를 저장하되, 블루레이 크기는 작을수록 좋다.
- 따라서 블루레이의 크기를 찾는 이분탐색 문제로 해결할 수 있다.

1. left는 max(lesson), right는 sum(lesson)로 설정한다.
2. left <= right일 동안 아래 과정을 반복한다.
3. 블루레이 크기를 중간값인 (left + right)//2로 지정한다.
4. 만약 파일 크기가 중간값을 넘어서면 cnt를 증가시키고 file에 영상을 저장한다.
5. 파일 크기가 아직 중간값보다 작다면 file에 영상을 더 추가한다.
6. 반복이 끝난 후 file에 영상이 남아있다면 cnt를 증가시킨다.
7. 최종 cnt가 m보다 크다면, 블루레이 크기가 작은 것이므로 left = mid+1
8. 최종 cnt가 m보다 작거나 같다면, 블루레이 크기가 큰 것이므로 answer에 중간값 저장 후 right = mid-1
9. 최종 answer를 출력한다.

## 2. [2110 공유기 설치](https://www.acmicpc.net/problem/2110)
![image](https://user-images.githubusercontent.com/44918665/128295606-440b3701-3008-47eb-9208-af5bbb95b3dc.png)
### 2.1. 문제유형
- Binary Search
### 2.2. 자료구조
- cnt (int): 공유기 개수
- left (int): 최소 거리 == 1
- right (int): 최대 거리 == (마지막 집 좌표 - 첫 번째 집 좌표)
- mid (int): 공유기 간 거리 == (left + right) // 2
- wifi (int): 공유기가 설치된 집 좌표
### 2.3. 해결과정
- 집 좌표 최대 크기가 10억이므로, 순차탐색이 아닌 이분탐색을 떠올려볼 것
- 공유기 간 최대거리를 찾는 것이 목적이므로 이분탐색 활용할 것
1. left <= right일 동안 아래 과정을 반복하며 중간값이 최대가 되는 값은 탐색한다.
2. 중간값 mid = (left+right)//2로, 최초 공유기 개수는 1, 최초 공유기 위치는 house[0]으로 설정한다.
3. 반복문을 돌며 2번째 집부터 마지막 집까지 아래 조건을 체크한다.
4. i번째 집 좌표가 이전 공유기 위치로부터 + 최대거리(중간값 mid)을 넘어서면 새로운 공유기를 설치하고, 공유기 개수를 증가시킨다.
5. 반복문 종료 후, 공유기 개수가 c보다 작다면 최대거리가 긴 것이므로 right = mid - 1
6. 공유기 개수가 c보다 크다면 최대거리가 짧은 것이므로 answer에 최대거리 저장 후 left = mid + 1
7. answer를 출력한다.
