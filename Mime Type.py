# https://www.codingame.com/training/easy/mime-type

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ext_l = []
mt_l = []
fname_l = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_l.append(ext.lower())
    mt_l.append(mt)
for i in range(q):
    fname = input()  # One file name per line.
    fname_l.append(fname)

for i in range(len(fname_l)):
    if '.' in fname_l[i]:
        ext = fname_l[i].split('.')[len(fname_l[i].split('.'))-1].lower()
        try:
            print(mt_l[ext_l.index(ext)])
        except Exception:
            print("UNKNOWN")
    else: print("UNKNOWN")
