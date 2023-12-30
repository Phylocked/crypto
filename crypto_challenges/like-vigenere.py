from crackrepeatkey import crack_cipher
filename = '7.txt'
with open(filename, 'r') as f:
    c = f.read().strip()
c_b = bytes.fromhex(c)
cracked, ks = crack_cipher(c_b)
cracked_s = cracked.decode()
print(cracked_s, ks)
