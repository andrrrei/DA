f = open('the_calls.txt')
fout = open('calls.txt', "w")
data = []
for line in f:
    data += [line.rstrip().split('\t')]
    
data.sort(key = lambda x: int(x[1]), reverse = True)
data_a = list(filter(lambda i: i[2] == 'A', data))
data_b = list(filter(lambda i: i[2] == 'B', data))

print(*(data_a + data_b)[0], file = fout, end = '', sep = '\t')
for data in (data_a + data_b)[1:]:
    print(file = fout)
    print(*data, file = fout, end = '', sep ='\t')

f.close()
fout.close()