from xor import byte_xor
from onebytexor import Score, find_best


def divide_txt(b_text: bytes, size: int) -> bytes:
    pass


def hamming_distance(b_t1: bytes, b_t2: bytes) -> int:
    pass


def divided_text(b_text: bytes, size: int) -> list:
    pass


def extract_bytes(ded_t: list, size: int) -> list:
if __name__ == '__main__':
    b_c = b'xxxxxxx'
    min_distance = int('inf')
    min_key_size = None
    for key_size in range(2, 41):
        b_c1, b_c2 = divide_txt(b_c, key_size)
        distance = hamming_distance(b_c1, b_c2)
        if distance < min_distance:
            min_distance = distance
            min_key_size = key_size
    d_ct = divided_text(b_c, min_key_size)
    e_ct = extract_bytes(d_ct, min_key_size)
    count = 0
    while count < min_key_size
