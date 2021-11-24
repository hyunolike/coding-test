// 첫번째 풀이
// 정렬 + if 문
Arrays.sort(participant);
Arrays.sort(completion); 

int i = 0; // i를 밖에서 인식하기 위해 따로 배치
for(i; i<completion.length;i++){
  if(!participant[i].equals(completion[i])){
    break;
  }
}
return participant[i];

// 두번째 문제 풀이
// 해시 사용
String answer = "";
HashMap<String, Integer> map = new HashMap<>();
for(String player : participant){
  map.put(player, map.getOrDefault(player, 0) + 1);
}
for(String player : completion){
  map.put(player, map.get(player) - 1);
}
Iterator<Map.Entry<String, Integer>> iter = map.entrySet().iterator();

while(iter.hasNext()){
  Map.Entry<String, Integer> entry = iter.next();
  if(entry.getValue != 0){
    answer = entry.getKey();
    break;
  }
}
return answer;
