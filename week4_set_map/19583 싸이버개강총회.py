import sys

st, ed, other = sys.stdin.readline().strip().split()
h, m = map(str, st.split(':'))
st = int(''.join([h,m]))
h, m = map(str, ed.split(':'))
ed = int(''.join([h,m]))
h, m = map(str, other.split(':'))
other = int(''.join([h,m]))
before = dict()
after = dict()
cnt = 0

while True:
    try:
        time, name = sys.stdin.readline().strip().split()
    except:
        break
    h, m = map(str, time.split(':'))
    time = int(''.join([h,m]))
    
    if time <= st:
        if time not in before.keys():
            before[name] = time
    elif ed <= time <= other:
        if name in before.keys() and name not in after.keys():
            after[name] = time
            cnt += 1
print(cnt)
