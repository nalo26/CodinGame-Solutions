# https://www.codingame.com/training/easy/defibrillators

from math import sqrt, cos

dmax = -1
lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
for i in range(n):
    defib = input()
    
    d_lon = float(defib.split(';')[4].replace(',', '.'))
    d_lat = float(defib.split(';')[5].replace(',', '.'))
    d = sqrt(pow(((d_lon - lon) * cos((lat + d_lat)/2)), 2)+pow((d_lat - lat), 2))*6371
    
    if d < dmax or dmax == -1:
        dmax = d
        answer = defib.split(';')[1]

print(answer)
