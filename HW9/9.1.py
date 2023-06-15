import itertools

for a, b, c in itertools.product([False, True], [False, True], [False, True]):
    if (not a and b and not c) or (not a and b and c) or (a and not b and not c):
        print(a, b, c)