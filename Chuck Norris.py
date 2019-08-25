# https://www.codingame.com/training/easy/chuck-norris

message = input()
binary_list = [bin(ord(ch))[2:].zfill(7) for ch in message]
binary = ''

for i in range(len(binary_list)): binary += binary_list[i]
l = []
s = 0
last = ''

for i in range(len(binary)):
    if binary[i] != last:
        l.append(binary[i])
        s += 1
    else: l[s-1] = l[s-1] + binary[i]
    last = binary[i]

final = ''
for i in range(len(l)):
    if str(l[i])[0] == '1': final += '0 '    
    if str(l[i])[0] == '0': final += '00 '
    for j in range(len(l[i])): final += '0'
    final += ' '
    
final = final[:-1]
print(final)
