f = open("input.txt", 'r')
strings = f.readlines()
f.close()
dict_animals = {}
for i in range(len(strings)):
    strings[i] = strings[i].split()
    if strings[i][1] in dict_animals:
        dict_animals[strings[i][1]] += 1
    else:
        dict_animals[strings[i][1]] = 1
sorted_animals = dict(sorted(dict_animals.items(), reverse = True, key = lambda x: x[1]))
for key,value in sorted_animals.items():
    print(key, '-', value)