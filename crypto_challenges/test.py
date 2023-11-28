def hamming_distance(b_t1: bytes, b_t2: bytes) -> int:
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(b_t1, b_t2))
b1 = b'this is a test'
b2 = b'wokka wokka!!!'
print(hamming_distance(b1, b2))