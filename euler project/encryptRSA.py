from math import gcd

p, q, s, e = 1009, 3643, 0, 3
phi = (p - 1) * (q - 1)

while (e < phi):
    if gcd(e, phi) == 1 and gcd(e - 1, q - 1) == 2 and gcd(e - 1, p - 1) == 2:
        s += e
    e += 4

print("Project Euler 182 Solution =", s)