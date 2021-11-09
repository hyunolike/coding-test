# 긴 쪽을 가로, 짧은 쪽을 세로라고 둘 것: 이후 가로, 세로 최대값 구하기
def solution(sizes):
    w,h=0,0
    for x,y in sizes:
        if x<y:
            x,y=y,x
        w=max(w, x)
        h=max(h, y)
    return w*h
