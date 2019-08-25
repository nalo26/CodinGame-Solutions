# https://www.codingame.com/training/easy/1d-spreadsheet

result = []
op_l = []
a1_l = []
a2_l = []

n = int(input())
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    op_l.append(str(operation))
    a1_l.append(str(arg_1))
    a2_l.append(str(arg_2))
    result.append('')

def calc(a, s, b, i):
    if str(a)[0] == '$':
        if result[int(a[1:])] != '': a1_l[i] = result[int(a[1:])]
        else: calc(a1_l[int(a[1:])], op_l[int(a[1:])], a2_l[int(a[1:])], int(a[1:]))
        a = result[int(a[1:])]
    if str(b)[0] == '$':
        if result[int(b[1:])] != '': a2_l[i] = result[int(b[1:])]
        else: calc(a1_l[int(b[1:])], op_l[int(b[1:])], a2_l[int(b[1:])], int(b[1:]))
        b = result[int(b[1:])]   
        
    if s == 'VALUE': result[i] = str(a)
    if s == 'ADD': result[i] = str(int(a) + int(b))
    if s == 'SUB': result[i] = str(int(a) - int(b))
    if s == 'MULT': result[i] = str(int(a) * int(b))
    
for i in range(n):
    if result[i] == '': calc(a1_l[i], op_l[i], a2_l[i], i)

for i in range(n):
    print(result[i])
