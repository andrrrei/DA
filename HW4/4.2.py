from fractions import Fraction

x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
z1, z2 = map(int, input().split())

a = Fraction(x1, x2)
b = Fraction(y1, y2)
c = Fraction(z1, z2)

d1 = float(Fraction(b, a) + Fraction(b, c + a) - Fraction(c, c - a))
print("{:.4f}".format(d1))