from collections import defaultdict
import sys

input = lambda : sys.stdin.readline()

S, E, Q = map(str, input().split())
s = int(''.join(S.split(":")))
e = int(''.join(E.split(":")))
q = int(''.join(Q.split(":")))

students = defaultdict(int)
count = 0

while True:
    try:
        time, student = map(str, input().split())
        t = int(''.join(time.split(":")))
        if t <= s:
            students[student] = 1

        elif e <= t <= q:
            if students[student] == 1:
                students[student] += 1
    except:
        break

list_of_value = list(students.values())
print(list_of_value.count(2))