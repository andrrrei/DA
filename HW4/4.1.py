x = int(input())
s = 0
iter = 1
while (x != 0) :
    s += x % 10 * iter
    x //= 10
    iter *= 2
print(s)