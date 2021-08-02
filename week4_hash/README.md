# 문제풀이

## [4195 친구 네트워크](https://www.acmicpc.net/problem/4195)

![image](https://user-images.githubusercontent.com/44918665/127806849-d560dcb7-45ec-477d-8ffa-2c7df6a64ee9.png)


### 📌풀이 유형
- Disjoint set(Union find), dictionary(set/map)

### 📌풀이 과정
1. 입력받은 x, y 친구를 그래프 그룹에 추가하고, 개수를 증가시킨다.
2. x, y의 부모노드를 받아온 뒤 한 부모 노드를 갖도록 합친다.
3. 합쳐진 부모 노드의 그래프 총 개수를 출력한다.

### 📌자료구조
parent (dictionary) : 친구 관계를 저장하는 dictionary
number (dictionary) : 친구 관계 그래프의 개수를 저장하는 dictionary

### 📌함수
1. getParent(x): x의 부모노드를 반환하는 재귀 함수
2. unionParent(x, y): x, y의 부모노드를 찾아 병합하는 함수

## [1302 베스트셀러](https://www.acmicpc.net/problem/1302)
![image](https://user-images.githubusercontent.com/44918665/127806860-5ee2083b-4a38-4d5b-9215-dd4c0172e225.png)

### 📌풀이 과정
1. dictionary에 책 이름을 저장하고, 개수를 카운트한다.
2. dictionary의 values가 최대값인 key를 반환한다.
