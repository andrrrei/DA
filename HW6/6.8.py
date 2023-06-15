f = open("input.txt", 'r')
strings = f.readlines()
f.close()
dict_animals = {}
for i in range(len(strings)):
    strings[i] = strings[i].split()
    if strings[i][1] in dict_animals:
        dict_animals[strings[i][1]].append(strings[i][0])
    else:
        dict_animals[strings[i][1]] = list()
        dict_animals[strings[i][1]].append(strings[i][0])
sort_list = sorted(list(dict_animals.keys()), key = lambda x: len(x))
for ke in sort_list:
    dict_animals[ke] = list(dict_animals[ke])
    dict_animals[ke].sort()
    print(ke+":", ', '.join(dict_animals[ke]))