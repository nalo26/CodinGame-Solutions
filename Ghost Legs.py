# https://www.codingame.com/training/easy/ghost-legs

T = []
B = []
L = []

w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    if i == 0: T = line.split()   # top
    if i == h-1: B = line.split() # bottom
    p = 0
    while p != -1:
        p = line.find('--', p+1)
        if p != -1: L.append(str(i)+'/'+str(int(p/3)+1)+'/'+str(int(p/3)+2))

for i in range(len(T)):
    pos = i+1
    for j in range(len(L)):
        x, a, b = L[j].split('/')
        #print(a, b, pos)
        if int(a) == pos: pos += 1
        elif int(b) == pos: pos -= 1
        
    print(T[i]+''+B[int(pos-1)])
