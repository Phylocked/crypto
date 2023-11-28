from onebytexor import find_best, calculate_score
from repeatingxor import repeat_xor
import base64


def divide_txt(b_text: bytes, size: int):
    return b_text[0: size], b_text[size: size+size]


def hamming_distance(b_t1: bytes, b_t2: bytes) -> float:
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(b_t1, b_t2))/len(b_t1)


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


def crack_cipher(b_c: bytes) -> tuple[bytes, int]:
    min_score = float('inf')
    best_plain = None
    best_key_size = None
    for key_size in range(2, 41):
        d_ct = divided_text(b_c, key_size)
        e_ct = extract_bytes(d_ct, key_size)
        key = b''
        for i in range(key_size):
            key += find_best(e_ct[i]).key
        cracked_text = repeat_xor(key, b_c)
        score = calculate_score(cracked_text)
        if score < min_score:
            min_score = score
            best_plain = cracked_text
            best_key_size = key_size
    return best_plain, best_key_size


if __name__ == '__main__':
    with open('6.txt', 'r') as f:
        cipher_t = f.read().strip()
    b_cipher_t = base64.b64decode(cipher_t)
    cracked, ks = crack_cipher(b_cipher_t)
    crack_t = cracked.decode()
    print(crack_t, ks)
