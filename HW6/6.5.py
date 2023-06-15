f = open("input.txt", 'r')
strings = f.readlines()
f.close()
animals = set()
for i in range (len(strings)):
    strings[i] = strings[i].split()
    animals.add(strings[i][1])
list_animals = list(animals)
list_animals.sort(key=lambda x: len(x))
for i in range (len(list_animals)):
    print(list_animals[i])
