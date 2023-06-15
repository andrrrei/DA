b, q, x = map(float, input().split())
elem = b
num = 1
while (elem < x) :
    elem *= q
    num += 1
print(num)