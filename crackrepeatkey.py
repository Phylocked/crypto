from onebytexor import find_best
from repeatingxor import repeat_xor


def divide_txt(b_text: bytes, size: int):
    return b_text[0: size], b_text[size: size+size]


def hamming_distance(b_t1: bytes, b_t2: bytes) -> int:
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(b_t1, b_t2))


def divided_text(b_text: bytes, size: int) -> list:
    return [b_text[i: i+size] for i in range(0, len(b_text), size)]


def extract_bytes(ded_t: list, size: int) -> list:
    b_list = []
    for i in range(size):
        b_machine = b''
        for block in ded_t:
            if i < len(block):
                b_machine += bytes([block[i]])
        b_list.append(b_machine)
    return b_list


def crack_cipher(b_c: bytes) -> bytes:
    min_distance = 10**100
    best_key_size = None
    for key_size in range(2, 41):
        b_c1, b_c2 = divide_txt(b_c, key_size)
        distance = hamming_distance(b_c1, b_c2)
        if distance < min_distance:
            min_distance = distance
            best_key_size = key_size
    d_ct = divided_text(b_c, best_key_size)
    e_ct = extract_bytes(d_ct, best_key_size)
    best_key = b''
    for i in range(best_key_size):
        best_key += find_best(e_ct[i]).key
        print(find_best(e_ct[i]).key)
    cracked_text = repeat_xor(best_key, b_c)
    return cracked_text


if __name__ == '__main__':
    with open('6.txt', 'r') as f:
        cipher_t = f.read().strip()
    b_cipher_t = cipher_t.encode()
    cracked = crack_cipher(b_cipher_t)
    print(cracked)
