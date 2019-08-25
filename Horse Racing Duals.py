# https://www.codingame.com/training/easy/horse-racing-duals

l = []
n = int(input())
for i in range(n):
    pi = int(input())
    l.append(pi)

l = sorted(l)
max = -1
for i in range(n):
    try: if abs(l[i+1] - l[i]) < max or max == -1: max = abs(l[i+1] - l[i])
    except Exception: pass

print(max)
