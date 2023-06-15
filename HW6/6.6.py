f = open("input.txt", 'r')
strings = f.readlines()
f.close()
dict_animals = {}
list_animals = []
for i in range(len(strings)):
    strings[i] = strings[i].split()
    if strings[i][1] in dict_animals:
        if (dict_animals[strings[i][1]] == "female" and strings[i][2] == "male") or (dict_animals[strings[i][1]] == "male" and strings[i][2] == "female"):
            dict_animals[strings[i][1]] = "ok"
            list_animals.append(strings[i][1])
    else:
        dict_animals[strings[i][1]] = strings[i][2]
list_animals.sort(key = lambda x: len(x))
if list_animals:
    for i in range(len(list_animals)):
        print(list_animals[i])
else:
    print(0)
    