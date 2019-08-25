# https://www.codingame.com/training/easy/temperatures

temp = 100000
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if temp < 0 and t*-1 == temp: temp = t
    elif abs(t) < abs(temp): temp = t
if temp == 100000: temp = 0
print(temp)
