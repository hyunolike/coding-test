n, m = int(input()), int(input())
frames = dict()

cnt = 0
for reco in map(int, input().split()):
    if len(frames) >= n and not reco in frames:
        del frames[min(frames, key=lambda x : frames[x])]
    try:
        frames[reco][0] += 1
    except:
        frames[reco] = [1, cnt]
print(*sorted(frames.keys()))