f = open('poe_unpublished.txt')
fout = open('poe_decode_attempt.txt', "w")
data = f.readlines()

data.sort(key = lambda x: len(x.split()))
for i in range(len(data)) :
    s = data[i].split()
    s.sort(key = lambda x: len(x))
    print(' '.join(map(str, s)), file = fout)
f.close()
fout.close()