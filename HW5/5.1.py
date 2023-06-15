f = open('weights.txt')
fout = open('team.txt', "w")
str = f.readlines()
name = 22 * [0]
weight = 22 * [0]
i = 0
for s in str :
    name[i], weight[i] =  s.split()
    weight[i] = float(weight[i])
    i += 1
data = list(zip(name, weight))
data.sort(key = lambda x: x[1], reverse = True)
for i in range(0, len(data), 2) :
    print(data[i][0], data[i][1], file = fout)
for i in range(1, len(data), 2) :
    print(data[i][0], data[i][1], file = fout)
f.close()
fout.close()