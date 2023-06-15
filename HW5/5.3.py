f = open('med_research.txt')
fout = open('output.txt', "w")
data = f.readlines()
n = len(data)
m = len(data[0].split())
a = []
for s in data :
    b = list(map(str, s.split()))
    a.append(b)
b = [['0' for j in range(n)] for i in range(m)]

for i in range(n):
    for j in range(m):
        b[j][i] = a[i][j]
for i in range(m):
    print(' '.join(map(str,b[i])), file = fout)
f.close()
fout.close()