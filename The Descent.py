# https://www.codingame.com/training/easy/the-descent

while True:
    hmax = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > hmax:
            hmax = mountain_h
            imax = i
    print(imax)
